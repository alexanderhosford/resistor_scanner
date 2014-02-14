import numpy as no
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('test.jpg',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show
