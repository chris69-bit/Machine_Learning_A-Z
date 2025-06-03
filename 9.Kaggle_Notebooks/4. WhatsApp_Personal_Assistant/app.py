from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/WhatsApp", methods=["POST"])

def reply_message():
    incoming_message = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hello" in incoming_message:
        msg.body("Hi👋, How can i help you today!")
    else:
        msg.body("Sorry, I didn't understand that. Try saying Niaje.")
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)