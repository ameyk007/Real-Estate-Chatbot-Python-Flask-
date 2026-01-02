from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def save_chat(user_msg, bot_msg):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO inquiries (user_message, bot_reply) VALUES (?, ?)",
        (user_msg, bot_msg)
    )
    conn.commit()
    conn.close()

def chatbot_response(message):
    msg = message.lower()

    if "buy" in msg:
        return "🏡 We have 2 BHK and 3 BHK flats available for purchase in Pune and Mumbai."

    elif "rent" in msg:
        return "🏠 Rental options available from ₹12,000 to ₹30,000 per month."

    elif "pune" in msg:
        return "📍 Pune properties include Hinjewadi, Wakad, and Kothrud areas."

    elif "mumbai" in msg:
        return "📍 Mumbai properties available in Andheri, Borivali, and Thane."

    elif "price" in msg or "budget" in msg:
        return "💰 Please share your budget so I can suggest suitable properties."

    elif "contact" in msg or "agent" in msg:
        return "📞 Our agent will contact you shortly. Please share your phone number."

    elif "hello" in msg or "hi" in msg:
        return "👋 Hello! How can I help you with buying or renting a property?"

    elif "bye" in msg:
        return "👋 Thank you for visiting DreamHome Real Estate!"

    else:
        return "❓ Sorry, I didn't understand. You can ask about buying, renting, or locations."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = chatbot_response(user_message)
    save_chat(user_message, bot_reply)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
