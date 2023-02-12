# QR Code Generator

Generates QR codes.

## Installation

Install [Python](https://python.org/) version 3.8 and [pip](https://pip.pypa.io/en/stable/)

Create a virtual environemnt by running
```bash
python3 -m venv .venv
```

Activate the environment by running command
```bash
source .venv venv/bin/activate
```

Install Qrcode and Image module by running command
```bash
pip3 install qrcode Image
```

## Usage

```python
import qrcode

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
```

## How to run the program
```python
python3 app.py
```
Deactivate virtual environment by simply running the below command
```python
deactivate
```

## License

[MIT](https://choosealicense.com/licenses/mit/)