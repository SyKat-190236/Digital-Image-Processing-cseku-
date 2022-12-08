import cv2

img = cv2.imread('abc.jpg',0)
img1 = cv2.imread('abc.jpg',0)

row, column = img.shape

min_range = int(input('Enter minimum range : '))
max_range = int(input('Enter maximum range : '))
amplitude = int(input('Enter amplitude : '))


for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img[i,j] = amplitude

cv2.imshow('Contrast stretched image', img)
cv2.imshow('original image', img1)
cv2.waitKey(0)