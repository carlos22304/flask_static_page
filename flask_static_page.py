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
    print("Running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)









