from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":
        message = request.form["note"]

    return render_template("home.html", message=message)

app.run(debug=True)
