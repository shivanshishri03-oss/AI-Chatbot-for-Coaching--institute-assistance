from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from chatbot import get_response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ---------------- DATABASE CONFIG ----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- DATABASE MODEL ----------------
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(500))
    bot_response = db.Column(db.String(500))


# ---------------- WEB ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    try:
        user_message = request.form["message"]
        response = get_response(user_message)

        chat = Chat(
            user_message=user_message,
            bot_response=response
        )
        db.session.add(chat)
        db.session.commit()

        return jsonify({"response": response})

    except Exception as e:
        print("WEB ERROR:", e)
        return jsonify({"response": "Error aaya hai 😢"})

@app.route("/admin")
def admin():
    chats = Chat.query.all()
    return render_template("admin.html", chats=chats)


# ---------------- WHATSAPP ROUTE ----------------
@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    try:
        # Get message from WhatsApp
        user_msg = request.form.get("Body")

        if not user_msg:
            user_msg = "hello"

        # Get bot response
        response = get_response(user_msg)

        if not response:
            response = "Sorry, main samajh nahi paya 😅"

        # Save to database
        chat = Chat(
            user_message=user_msg,
            bot_response=response
        )
        db.session.add(chat)
        db.session.commit()

        # Twilio response
        reply = MessagingResponse()
        msg = reply.message()
        msg.body(response)

        return str(reply)

    except Exception as e:
        print("WHATSAPP ERROR:", e)

        reply = MessagingResponse()
        reply.message("Server error aaya hai 😢")

        return str(reply)


# ---------------- CREATE DB & RUN ----------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, use_reloader=False)  