from flask import Flask, render_template, request
from utils.qr_generator import generate_qr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")

        if not url:
            error = "Please enter a valid URL."
        else:
            qr_path = generate_qr(url)

    return render_template("index.html", qr_path=qr_path, error=error)


if __name__ == "__main__":
    app.run(debug=True)
