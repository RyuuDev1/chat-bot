
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}  # Replace with your API key

# Store chat history for each user session
chat_history = []

def get_ai_response(prompt, history):
    # Combine history with current prompt
    full_prompt = "\n".join(history + [prompt])
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": full_prompt})
    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        return "Oops! Something went wrong. 💔"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    chat_history.append("User: " + user_message)
    bot_reply = get_ai_response(user_message, chat_history)
    chat_history.append("Valentine Girl: " + bot_reply)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
