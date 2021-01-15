import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("He/She is the student of Bandarban University")
qr.png("MyQr  .png")