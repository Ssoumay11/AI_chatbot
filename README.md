🤖 AI Chatbot Agents – Streamlit UI
A simple Streamlit-based user interface for interacting with AI chatbot agents via a /chat backend API.

✨ Features
Define a system prompt for your agent
Choose between Groq and OpenAI models
Enable/disable web search support
Get structured AI responses in real-time

🛠️ Tech Stack
Streamlit
 – Frontend UI
Python requests
 – API calls
Groq
 & OpenAI
 APIs – LLM backends

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/ai-chatbot-agents-ui.git
cd ai-chatbot-agents-ui
2. Create & activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

4. Install dependencies
pip install -r requirements.txt

5. Set up environment variables
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
CHAT_BACKEND_URL=http://localhost:8000/chat

6. Run the Streamlit app
streamlit run app.py
📸 Screenshots
(Add some screenshots of your UI here!)
🔮 Roadmap
 Conversation history
 Support for multiple agents
 Save & load prompts
 UI improvements (dark mode, layout)

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License

MIT License – feel free to use this project as you like.
