import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
genai.configure(api_key=api_key)

try:
    with open("knowledge_base.txt", "r", encoding="utf-8") as f:
        knowledge_base = f.read()
except FileNotFoundError:
    print("Warning: knowledge_base.txt not found. The copilot will have no context.")
    knowledge_base = ""

SYSTEM_PROMPT = f"""
You are an expert HR Copilot for our company. Your role is to assist employees by answering their questions accurately and politely.
You MUST base your answers strictly on the information provided in the following internal knowledge base.
If the answer is not found in the knowledge base, you MUST explicitly state, "I'm sorry, I don't have information on that topic. Please contact the HR department for assistance."
Do not invent, hallucinate, or provide information from outside of this context.

--- KNOWLEDGE BASE ---
{knowledge_base}
--- END KNOWLEDGE BASE ---
"""

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=SYSTEM_PROMPT
)

@app.route('/ask', methods=['POST'])
def ask_copilot():
    user_question = request.json.get('question')

    if not user_question:
        return jsonify({"error": "No question provided."}), 400

    print(f"Received question: {user_question}")

    try:
        response = model.generate_content(user_question)
        ai_response = response.text

        print(f"AI Response: {ai_response}")
        return jsonify({"answer": ai_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to get a response from the AI model."}), 500

@app.route('/')
def index():
    return "HR Copilot Backend is running!"