import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load env variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3-flash-preview")

chat = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "You are a great translator. Translate each given word or phrase "
                    "or even a sentence into the given language in the prompt and nothing more. "
                    "Don't add extra phrases, just the translation."
                )
            }],
        }
    ]
)

# Home page (CS50 style)
@app.route("/")
def index():
    return render_template("index.html")

# AJAX endpoint
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text")
    lang = data.get("lang")

    if not text or not lang:
        return jsonify({"error": "Missing data"}), 400

    result = chat.send_message(
        f'Translate "{text}" into {lang}'
    )

    return jsonify({
        "translation": result.text
    })
    

if __name__ == "__main__":
    app.run(debug=True)
