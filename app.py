
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": "Bearer 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 "}  # Replace with your API key

def get_ai_response(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        return "Oops! Something went wrong. 💔"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    bot_reply = get_ai_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
