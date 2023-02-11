import sys
import qrcode
from pathlib import Path
from subprocess import call


def generate_qrcode(source):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(source)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white")

    print("Opening QR code...")

    # determine the saved png path
    qr_path = Path(sys.path[0])/'qr.png'

    # open the saved file
    call(["open", qr_path])

try:
    source = input("Enter your text: ")
    generate_qrcode(source)
    # pass
except:
    print("EOF")

sys.exit()