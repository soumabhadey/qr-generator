from flask import Flask, render_template, request
import qrcode
from PIL import Image
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/qr_code")
def qr_code():
    text = request.args.get("text")

    output_folder = os.path.join(app.root_path, "static")
    filename = f"{text}.png"
    generate_qr_code(text, output_folder, filename)

    qr_image_path = os.path.join("static", filename)

    return render_template("qr_code.html", text=text, qr_image=qr_image_path)


def generate_qr_code(text, output_folder, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image to the specified folder
    qr_img_path = os.path.join(output_folder, filename)
    qr_img.save(qr_img_path)