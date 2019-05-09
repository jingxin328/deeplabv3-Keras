from matplotlib import pyplot as plt
import cv2
import numpy as np
from model import Deeplabv3


deeplab_model = Deeplabv3(weights='cityscapes', input_shape=(1024, 2048, 3), classes=19,  OS=16)
deeplab_model.load_weights('models\deeplabv3_mobilenetv2_tf_dim_ordering_tf_kernels_cityscapes.h5', by_name=True)
deeplab_model.summary()

img = plt.imread("imgs/1001.png")
print(img.shape)
res = deeplab_model.predict(np.expand_dims(img, 0))
print(res.shape)
labels = np.argmax(res.squeeze(), -1)
plt.imshow(labels)
plt.show()


