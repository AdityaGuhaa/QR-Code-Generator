import qrcode
import os
from datetime import datetime


def cleanup_old_qrs(directory: str, max_files: int = 30):
    if not os.path.exists(directory):
        return

    files = sorted(
        [os.path.join(directory, f) for f in os.listdir(directory)],
        key=os.path.getctime
    )

    while len(files) > max_files:
        os.remove(files.pop(0))


def generate_qr(
    data: str,
    fill_color: str = "black",
    back_color: str = "white",
    save_dir: str = "static/qr_codes"
) -> str:

    os.makedirs(save_dir, exist_ok=True)

    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.png"
    file_path = os.path.join(save_dir, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )
    img.save(file_path)

    cleanup_old_qrs(save_dir)
    return file_path
