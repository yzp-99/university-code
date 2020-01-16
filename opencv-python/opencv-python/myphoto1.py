

from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# cv2读取图片
img = cv2.imread('yu.jpg')  # 名称不能有汉字
cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
pilimg = Image.fromarray(cv2img)

# PIL图片上打印汉字
draw = ImageDraw.Draw(pilimg)  # 图片上打印
font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8")  # 参数1：字体文件路径，参数2：字体大小
draw.text((0, 0), "Hi,我是诗shi", (255, 0, 0), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体

# PIL图片转cv2 图片
cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
# cv2.imshow("图片", cv2charimg) # 汉字窗口标题显示乱码
cv2.imshow("photo", cv2charimg)

cv2.waitKey(0)
cv2.destroyAllWindows()