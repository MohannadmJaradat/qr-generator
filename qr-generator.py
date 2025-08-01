import pyqrcode
from PIL import Image
link = input("Enter the link to generate QR code: ")
qr = pyqrcode.create(link)
qr.png('qr_code.png', scale=8)
img = Image.open('qr_code.png')
img.show()
