from matplotlib import pyplot as plt
import cv2
import numpy as np
from model import Deeplabv3

deeplab_model = Deeplabv3(input_shape=(384, 384, 3), classes=4)
