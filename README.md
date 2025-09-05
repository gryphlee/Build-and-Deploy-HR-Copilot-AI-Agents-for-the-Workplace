HR Copilot AI Agent
🚀 Overview
This project is a smart, internal HR assistant built to answer employee questions based on a company-specific knowledge base. It uses the Google Gemini API to understand natural language queries and provide accurate, context-aware responses. The goal is to provide employees with instant access to HR information, reducing the workload on the HR department and improving employee experience.

📸 Demo
Here's a quick look at the HR Copilot in action:

✨ Key Features
Conversational AI: Utilizes a powerful language model to understand and respond to user questions.

Custom Knowledge Base: Answers are strictly based on the content provided in knowledge_base.txt, ensuring accuracy and relevance to company policies.

Secure & Private: The model is instructed not to use external information, keeping company data private.

Simple Web Interface: A clean and user-friendly chat interface for easy interaction.

Easily Extensible: The knowledge base can be expanded by simply editing a text file.

🛠️ Technology Stack
Backend: Python 3, Flask

AI Model: Google Gemini 1.5 Flash

Frontend: HTML, CSS, JavaScript (no frameworks)

Python Libraries: google-generativeai, python-dotenv, Flask-Cors

📁 Project Structure
hr-copilot/
├── venv/                 # Virtual environment directory
├── app.py                # The main Flask application (backend server)
├── index.html            # The chat interface (frontend)
├── knowledge_base.txt    # The source of truth for all HR policies
├── .env                  # Stores the API key securely
├── requirements.txt      # Lists all Python dependencies
└── README.md             # This documentation file

⚙️ Setup and Installation
Follow these steps to get the project running on a new machine.

Clone or Download: Get the project files onto your local machine.

Navigate to Directory: Open a terminal or command prompt and navigate into the project folder.

cd path/to/hr-copilot

Create a Virtual Environment:

python -m venv venv

Activate the Virtual Environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install Dependencies: Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt

🔑 Configuration
Create a .env file in the root of the project directory.

Add your API key to the .env file in the following format:

GEMINI_API_KEY="YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with your actual Google Gemini API key.

🧠 Customizing the Knowledge Base
To add, remove, or update the HR policies, simply edit the knowledge_base.txt file. The AI will automatically use the updated information the next time the server is restarted. Use clear headings with ### for better organization.

▶️ Running the Application
Start the Backend Server: Make sure your virtual environment is activated. Run the following command in your terminal:

flask run

The server will start, typically on http://127.0.0.1:5000.

Open the Frontend: In your file explorer, find and double-click the index.html file to open it in your web browser.

You can now start chatting with your HR Copilot!

🤖 How It Works
The application uses a technique similar to Retrieval-Augmented Generation (RAG).

The entire content of knowledge_base.txt is loaded into a SYSTEM_PROMPT when the Flask server starts.

This system prompt instructs the Gemini model to act as an HR Copilot and to only use the provided text as its source of truth.

When a user asks a question, it is sent to the Gemini model, which then generates an answer based on the instructions and the knowledge base it was given.

🔮 Future Enhancements
Implement a Vector Database: For very large documents (e.g., 100+ page handbooks), convert the knowledge base into a vector database (like ChromaDB or Pinecone) for more efficient and scalable information retrieval.

User Authentication: Add a login system to track conversations or provide personalized information.

Conversation History: Store and display the history of the user's conversation.

Deployment: Deploy the application to a cloud service (like Google Cloud Run or Vercel) so it can be accessed by anyone in the company.
