import cv2
import numpy as np

img = cv2.imread('abc.jpg')

rows = img.shape[0]*2
cols = img.shape[1]*2
levs = 3

zoomed = np.zeros((rows, cols, levs), dtype=img.dtype)

for i in range(0, rows):
    for j in range(0, cols):
            zoomed[i, j] = img[int(i / 2), int(j / 2)]

srows = int(img.shape[0]/4)
scols = int(img.shape[1]/4)

shrink = np.zeros((srows, scols, levs), dtype=img.dtype)

for i in range(0, srows):
    for j in range(0, scols):
            shrink[i, j] = img[i*4, j*4]

#print(img.shape)
cv2.imshow('Original Image', img)
cv2.imshow('zoom', zoomed)
cv2.imshow('shrink', shrink)
cv2.waitKey(0)