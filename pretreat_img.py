from PIL import Image
import os

image_folder = "imgs"

files = os.listdir(image_folder)
photo_num = 0

for file in files:  # 遍历文件夹
    im=Image.open(image_folder + "/" + file)  # 打开文件
    im.convert('RGB').save(image_folder + "/"+str(photo_num)+".jpg", "JPEG")
    photo_num = photo_num+1
print(photo_num, 'photo change!')



