from flask import Flask, render_template, request, jsonify, session
from urllib.parse import urlparse
from utils.qr_generator import generate_qr
import os

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")
PORT = int(os.environ.get("PORT", 5000))
DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    error = None

    session.setdefault("history", [])

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        fill = request.form.get("fill_color", "black")
        back = request.form.get("back_color", "white")

        if not is_valid_url(url):
            error = "Enter a valid URL (http:// or https://)"
        else:
            qr_path = generate_qr(url, fill, back)
            session["history"].append(qr_path)
            session.modified = True

    return render_template(
        "index.html",
        qr_path=qr_path,
        error=error,
        history=session["history"]
    )

@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(force=True)

    url = data.get("url")
    fill = data.get("fill_color", "black")
    back = data.get("back_color", "white")

    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    qr_path = generate_qr(url, fill, back)
    return jsonify({"qr_code_path": qr_path}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
