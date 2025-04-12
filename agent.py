import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# ---------- CONFIG ----------
# Set API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Load BLIP for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(image):
    raw_image = Image.open(image).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Set up LangChain agents
llm = ChatOpenAI(temperature=0)  # It automatically uses the env variable

agent1_prompt = PromptTemplate.from_template(
    "You are a property inspection assistant. Given an image caption and user query, detect issues and suggest fixes.\n\nImage Caption: {caption}\nUser Text: {text}\nAnswer:"
)
agent1_chain = LLMChain(llm=llm, prompt=agent1_prompt)

agent2_prompt = PromptTemplate.from_template(
    "You are a legal assistant for tenancy-related questions. Provide jurisdiction-specific, helpful answers.\n\nUser Question: {input}\nAnswer:"
)
agent2_chain = LLMChain(llm=llm, prompt=agent2_prompt)

# Routing logic
def route_agent(image, text):
    if image is not None:
        return "agent1"
    keywords = ["notice", "evict", "deposit", "landlord", "tenant", "rent", "contract"]
    if any(word in text.lower() for word in keywords):
        return "agent2"
    return "ask"

# ---------- UI ----------
st.set_page_config(page_title="🏠 Real Estate Multi-Agent Bot")
st.title("🏠 Multi-Agent Real Estate Chatbot")

st.write("Ask about property issues or tenancy laws. Upload an image if reporting a physical problem.")

image = st.file_uploader("Upload a property image (optional)", type=["png", "jpg", "jpeg"])
text_input = st.text_area("Enter your question or context")

if st.button("Submit"):
    if not text_input and not image:
        st.warning("Please provide some input.")
    else:
        agent = route_agent(image, text_input)

        if agent == "agent1":
            st.info("Routing to Property Issue Agent 🛠️")
            with st.spinner("Analyzing image..."):
                caption = caption_image(image)
                result = agent1_chain.run({"caption": caption, "text": text_input})
            st.success(result)

        elif agent == "agent2":
            st.info("Routing to Tenancy FAQ Agent 📄")
            with st.spinner("Fetching legal advice..."):
                result = agent2_chain.run({"input": text_input})
            st.success(result)

        else:
            st.warning("Not sure how to help. Is this about a property issue or a legal question?")
