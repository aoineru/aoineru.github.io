from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini APIキーを設定
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# === ① フロントエンドのHTMLを返すルートを追加 ===
@app.route("/")
def serve_index():
    return send_from_directory(os.path.dirname(__file__), 'index.html') # index.html を返す

# === ② ユーザーの入力を受け取ってAI応答を返すAPIエンドポイント ===
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    response = model.generate_content(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)

