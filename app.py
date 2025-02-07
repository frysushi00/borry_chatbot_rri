import pickle
from flask import Flask, request, jsonify, render_template
from util import JSONParser
from bot import bot_response, preprocess  

app = Flask(__name__)


with open("model_chatbot.pkl", "rb") as model_file:
    pipeline = pickle.load(model_file)


path = "data/intents.json"
jp = JSONParser()
jp.parse(path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "Saya tidak mengerti"}), 400

    print("[DEBUG] Menerima input:", user_input)  
    
    try:
        response, _ = bot_response(user_input, pipeline, jp)
        print("[DEBUG] Bot response:", response)  
    except Exception as e:
        print("[ERROR]", e) 
        return jsonify({"response": "Terjadi kesalahan pada server"}), 500

    return jsonify({"response": response})

if __name__ == "__main__":
    print("[INFO] Flask server mulai...")
    app.run(debug=True)
    print("[INFO] Flask server sudah berhenti.")  
