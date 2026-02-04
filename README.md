# 🔗 QR Code Generator – Flask Web App

A full-stack **Flask-based QR Code Generator** that allows users to generate downloadable QR codes from URLs, customize QR colors, maintain session-based history, and access QR generation via a REST API.  
The application is **Dockerized**, production-ready, and deployable on modern cloud platforms.

---

## 🚀 Features

- ✅ Generate QR codes from valid URLs
- 🎨 Customize QR foreground & background colors
- 📜 Session-based QR history (per user session)
- 🌐 REST API endpoint for QR generation
- 🐳 Dockerized for consistent deployment
- 🧹 Automatic cleanup of old QR images
- 🔐 Input validation & error handling

---

## 🛠 Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python, Flask |
| QR Generation | `qrcode`, `Pillow` |
| Frontend | HTML, CSS |
| Containerization | Docker |
| API | REST (JSON) |

---

## 📂 Project Structure

```plaintext
qr-code-webapp/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
├── .dockerignore           # Docker ignore rules
├── README.md               # Project documentation
│
├── utils/
│   └── qr_generator.py     # QR generation & cleanup logic
│
├── templates/
│   └── index.html          # Web UI template
│
├── static/
│   ├── css/
│   │   └── style.css       # Styling
│   └── qr_codes/           # Generated QR images
