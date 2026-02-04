from flask import Flask, render_template, request
from urllib.parse import urlparse
from utils.qr_generator import generate_qr

app = Flask(__name__)


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    error = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if not url:
            error = "URL cannot be empty."
        elif not is_valid_url(url):
            error = "Please enter a valid URL starting with http:// or https://"
        else:
            qr_path = generate_qr(url)

    return render_template("index.html", qr_path=qr_path, error=error)


if __name__ == "__main__":
    app.run(debug=True)
