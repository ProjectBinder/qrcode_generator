# QR Code Generator

This repository contains a Python script for generating QR codes. The script takes a URL as input and outputs a QR code image.

## Features

- Generates QR codes from URLs
- Customizable size and error correction level
- Outputs QR codes as PNG images

## Requirements

- Python 3.6+
- `qrcode` library
- `Pillow` library (for image processing)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

2. Install the required libraries:

```bash
pip install qrcode[pil]
```

## Usage

1. Rename your script file to avoid naming conflicts, e.g., `generate_qrcode.py`.
2. Update the script with the desired URL:

```python
# URL to be encoded in the QR code
url = "https://projectbinder-pib.atlassian.net/servicedesk/customer/portals"
```

3. Run the script:

```bash
python generate_qrcode.py
```

The QR code image will be saved as `pib_help_center_qr.png` in the current directory.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have any questions or suggerstions, please feel free to contact me at [kasper.telkamp@projectbinder.eu]