import numpy
n = numpy.arange(27)
n

n.reshape(3, 3, 3)

import cv2
img = cv2.imread('smallgray.png', 0) # 0 for grayscale reading
img

img = cv2.imread('smallgray.png', 1) # 1 for bgr(blue, green, red) reading
img

cv2.imwrite('newsmallgray.png', img)
