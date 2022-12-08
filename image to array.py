import cv2
import numpy as np

img = cv2.imread('berlin.jpg')
img1 = cv2.imread('berlin.jpg', 0)
imgarr = np.array(img)

print(imgarr)

cv2.imwrite('new.jpg',imgarr)

cv2.imshow('Imput image', img)
cv2.imshow('Gray image', img1)
cv2.waitKey(0)