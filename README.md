# QR Code Generator Web App

A full‑stack Flask-based web application that allows users to generate QR codes from URLs with customizable colors. The application supports a clean web UI, a REST API, session-based QR history, and Dockerized deployment for consistency across environments.

This project is designed to demonstrate real-world backend engineering practices, including environment-based configuration, modular code structure, Docker workflows, and production-ready deployment patterns.

---

## Features

* Web interface to generate QR codes from URLs
* Customizable QR foreground and background colors
* Session-based QR code history per user
* REST API endpoint for programmatic QR generation
* Automatic cleanup of old QR images
* Dockerized setup for reproducible builds
* Environment-based configuration for ports and secrets

---

## Tech Stack

* **Backend:** Python, Flask
* **QR Generation:** qrcode, Pillow
* **Frontend:** HTML, CSS (Jinja2 templates)
* **Containerization:** Docker
* **Runtime:** Gunicorn-ready (Flask app structured for production WSGI servers)

---

## Project Structure

```
qr-code-webapp/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build configuration
├── .dockerignore          # Docker ignore rules
├── README.md              # Project documentation
│
├── utils/
│   └── qr_generator.py    # QR generation and cleanup logic
│
├── templates/
│   └── index.html         # Web UI template
│
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── qr_codes/          # Generated QR images
```

---

## Local Development (Without Docker)

### 1. Create and activate Conda environment

```bash
conda create -n qrcode python=3.11 -y
conda activate qrcode
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

Open your browser at:

```
http://127.0.0.1:5000
```

---

## Running with Docker

### 1. Build Docker image

```bash
docker build -t qr-generator .
```

### 2. Run Docker container

```bash
docker run -p 5001:5000 qr-generator
```

Open your browser at:

```
http://localhost:5001
```

---

## REST API Usage

### Endpoint

```
POST /api/generate
```

### Request (JSON)

```json
{
  "url": "https://example.com",
  "fill_color": "black",
  "back_color": "white"
}
```

### Response

```json
{
  "qr_code_path": "static/qr_codes/qr_20260204_232200.png"
}
```

---

## Environment Variables

| Variable    | Description          | Default        |
| ----------- | -------------------- | -------------- |
| PORT        | Application port     | 5000           |
| SECRET_KEY  | Flask session secret | dev-secret-key |
| FLASK_DEBUG | Enable debug mode    | 0              |

---

## Notes on Production Deployment

* The application is structured to work with production WSGI servers like Gunicorn.
* Docker is recommended for deployment to platforms such as Render, Railway, or Fly.io.
* Debug mode is disabled by default for safety.

---

## Future Improvements

* Add Gunicorn as the default production server
* Persistent database-backed QR history
* Authentication and user accounts
* Rate limiting and security hardening
* QR code expiration policies

---

## License

This project is open-source and intended for educational and learning purposes.

---
