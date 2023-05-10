import pyqrcode
from pyqrcode import QRCode
import png
github_acc = "https://github.com/Navyasri84"
url= pyqrcode.create(github_acc)
url.show(png,scale=10)