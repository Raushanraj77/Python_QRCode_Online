from pyzbar.pyzbar import decode
import requests
from PIL import Image
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/1200px-QR_code_for_mobile_English_Wikipedia.svg.png'
fileName = 'sample.png'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
decode(Image.open('sample.png'))
print (decode(Image.open('barcode.png')))


