'''
==============================
qr2：生成二维码及查看
==============================
'''
from PIL import Image
import qrcode

qr = qrcode.QRCode(
    version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
qr.add_data("于宗鹏")
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon = Image.open("qing.jpg")  # 这里是二维码中心的图片

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)
img.show()   # 显示图片,可以通过save保存
#imObj.save('qin.png', quality=95)
