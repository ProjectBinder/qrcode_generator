import qrcode

# URL to be encoded in the QR code
url = "https://projectbinder-pib.atlassian.net/servicedesk/customer/portals"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill='black', back_color='white')

# Save the image
img_path = "pib_help_center_qr.png"  # Save in the current directory
img.save(img_path)

img_path
