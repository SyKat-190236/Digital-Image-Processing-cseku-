import numpy as np
import cv2

img = cv2.imread('abc.jpg', 0)


lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j], width=8))

eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0], img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0], img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0], img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0], img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0], img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0], img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0], img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0], img.shape[1])

new_img = eight_bit_img+seven_bit_img+six_bit_img+five_bit_img+four_bit_img+three_bit_img+two_bit_img+one_bit_img

flag = int(input('Please Enter Sequence Number of Bit to OFF :'))

if(flag==1):
    new_img = new_img - one_bit_img
elif(flag==2):
    new_img = new_img - two_bit_img
elif(flag==3):
    new_img = new_img - three_bit_img
elif(flag==4):
    new_img = new_img - four_bit_img
elif(flag==5):
    new_img = new_img - five_bit_img
elif(flag==6):
    new_img = new_img - six_bit_img
elif(flag==7):
    new_img = new_img - seven_bit_img
elif(flag==8):
    new_img = new_img - eight_bit_img

cv2.imshow('Original image', img)
cv2.imshow('Bit Plane Slicing', new_img)
cv2.waitKey(0)