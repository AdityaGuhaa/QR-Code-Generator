import qrcode
import os
from datetime import datetime


def generate_qr(url: str, save_dir: str = "static/qr_codes") -> str:

    os.makedirs(save_dir, exist_ok=True)

    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = os.path.join(save_dir, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    return file_path
