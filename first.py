import numpy as np
import cv2 as cv

img = cv.imread('/Users/Panda/Desktop/DSC_0042.JPG',0)

cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey() & 0xFF
cv.destroyAllWindows()


