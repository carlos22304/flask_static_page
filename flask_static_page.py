from flask import Flask, render_template

app = Flask(__name__)


from flask import Flask, render_template
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.json.get("message", "")
        response = generate_response(user_input)
        return jsonify({"response": response})
    return render_template("chat.html")

def generate_response(message):
    if "river" in message.lower():
        return "The Tennessee River flows through Chattanooga and is key to its history."
    elif "civil war" in message.lower():
        return "Chattanooga was a strategic location during the American Civil War."
    else:
        return "Welcome to Chattanooga! Feel free to ask about its history, nature, or attractions."









