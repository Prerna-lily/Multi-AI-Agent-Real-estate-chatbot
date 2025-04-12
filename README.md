**🏠 Multi-Agent Real Estate Chatbot**
This Streamlit app uses two specialized AI agents to help users with real estate-related inquiries. It can:

Analyze uploaded property images and suggest potential issues or fixes.

Answer tenancy-related legal questions.

Built using LangChain, OpenAI, Hugging Face Transformers, and Streamlit.

🚀 Features
🔍 Property Issue Assistant (Agent 1):
Upload a property image and describe your issue. The assistant will inspect the image and suggest possible fixes based on the detected problem.

📜 Tenancy Legal Assistant (Agent 2):
Ask tenancy-related legal questions (like eviction, rent, or deposit issues), and receive jurisdiction-aware assistance.

🧠 Smart Agent Routing:
Automatically routes your query to the appropriate agent based on image presence and text keywords.

🛠️ Tech Stack
Streamlit

Hugging Face Transformers

BLIP (Image Captioning): Salesforce/blip-image-captioning-base

LangChain

OpenAI GPT (via LangChain ChatOpenAI)

📦 Setup Instructions
1. Clone the Repository
bash

git clone https://github.com/your-username/multi-agent-chatbot.git
cd multi-agent-chatbot
2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies
bash

pip install -r requirements.txt
If you don’t have a requirements.txt, use:

bash

pip install streamlit transformers torch pillow langchain openai
4. Set Your OpenAI API Key
In app.py, replace:

python

openai_api_key = ""
With your OpenAI API key:

python

openai_api_key = ""
Or you can use environment variables for better security.

🧪 Run the App
bash

streamlit run app.py
Then, open your browser to http://localhost:8501.

📁 File Structure
bash

multi_agent_chatbot/
│
├── agent.py              # Main Streamlit application
├── README.md           # You're here!
└── requirements.txt    # Python dependencies (recommended)

📸 Example Use Cases
Upload Image + Text
“This wall seems damaged near the pipe. Is it safe?”
→ Agent 1 will analyze the image and provide advice.

Text-only Question
“Can my landlord evict me without a notice?”
→ Agent 2 will answer with legal guidance.

🔒 Notes
Your OpenAI API usage will be billed under your account.

The app does not currently support jurisdiction detection—answers are general unless customized further.

