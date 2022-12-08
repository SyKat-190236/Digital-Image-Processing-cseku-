import cv2
import numpy as np

img = cv2.imread('abc.jpg',0)

row, col = img.shape

blur = np.zeros_like(img)
gauss = np.zeros_like(img)

filter = np.array([[1,1,1],[1,1,1],[1,1,1]])
filter_g = np.array([[1,2,1],[2,4,2],[1,2,1]])

for i in range(row-2):
    for j in range(col-2):
        blur[i,j] = (np.sum(img[i:i+3,j:j+3]*filter))/9

for i in range(row-2):
    for j in range(col-2):
        gauss[i,j] = (np.sum(img[i:i+3,j:j+3]*filter_g))/16

laplacian = np.zeros_like(img)
gradient = np.zeros_like(img)

laplacian_filter = np.array([[1,1,1],[1,-8,1],[1,1,1]])
gradient_filterx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gradient_filtery = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])


for i in range(row-2):
    for j in range(col-2):
        laplacian[i,j] = img[i,j]-(np.sum(img[i:i+3,j:j+3]*laplacian_filter))
        gradient[i,j] = img[i,j]-((np.sum(img[i:i+3,j:j+3]*gradient_filterx)) + (np.sum(img[i:i+3,j:j+3]*gradient_filtery)))

robert_x = np.array([[-1,0],[0,1]])
robert_y = np.array([[0,-1],[1,0]])
robert = np.zeros_like(img)

for i in range(row-1):
    for j in range(col-1):
        robert[i,j] = img[i,j]-((np.sum(img[i:i+2,j:j+2]*robert_x))+np.sum(img[i:i+2,j:j+2]*robert_y))

inp = int(input("Enter 1 for Bluring Enter 2 for Sharpening : "))

if(inp==1):
    cv2.imshow('Original', img)
    cv2.imshow('Averaging', blur)
    cv2.imshow('weighted average',gauss)
    cv2.waitKey(0)
elif(inp==2):
    cv2.imshow('Original', img)
    cv2.imshow('Laplacian', laplacian)
    cv2.imshow('Sobel', gradient)
    cv2.imshow('Robert', robert)
    cv2.waitKey(0)



