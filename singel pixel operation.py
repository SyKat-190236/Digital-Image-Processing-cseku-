import cv2
import numpy as np

img1 = cv2.imread('org.jpg')
img2 = 255-img1-1

img_log = (np.log(img1+1)/(np.log(1+np.max(img1))))*255
img_log = np.array(img_log, dtype=np.uint8)

r = float(input("Enter the value of Gamma: "))
gamma1 = np.array(255*(img1/255)**r, dtype='uint8')

cv2.imshow('Input image', img1)
cv2.imshow('Negative image', img2)
cv2.imshow('Log image', img_log)
cv2.imshow('Gamma Transformation', gamma1)
cv2.waitKey(0)