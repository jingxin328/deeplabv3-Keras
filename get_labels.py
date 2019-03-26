from matplotlib import pyplot as plt
import cv2  # used for resize. if you dont have it, use anything else
import numpy as np
from model import Deeplabv3


deeplab_model = Deeplabv3()
img = plt.imread("imgs/250.jpg")
print(img.shape)
w, h, _ = img.shape
ratio = 512. / np.max([w, h])
resized = cv2.resize(img, (int(ratio*h), int(ratio*w)))
resized = resized / 127.5 - 1.
pad_x = int(512 - resized.shape[0])
resized2 = np.pad(resized, ((0, pad_x), (0, 0), (0, 0)), mode='constant')
res = deeplab_model.predict(np.expand_dims(resized2, 0))
labels = np.argmax(res.squeeze(), -1)
print(labels.shape)
plt.imshow(labels[:-pad_x])
plt.axis('off')  # 关闭坐标轴
frame = plt.gca()
# y 轴不可见
frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
frame.axes.get_xaxis().set_visible(False)
# plt.savefig('imgs/result_250.jpg')
plt.show()


