import pyqrcode
from pyqrcode import QRCode

# Generate a QR code with error correction
qr_data = "Hello, world!"
qr = pyqrcode.create(qr_data, error='h')  # 'h' for high error correction
qr.png('qr_with_error_correction.png', scale=5)
