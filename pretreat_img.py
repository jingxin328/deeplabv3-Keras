from PIL import Image

image_path="imgs/000018.jpg"
im = Image.open(image_path)
im.convert('RGB').save("imgs/000001.jpg", "JPEG")  #this converts png image as jpeg
