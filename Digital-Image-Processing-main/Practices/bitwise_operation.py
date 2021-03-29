import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('images/bowlboy.jpeg')
img2 = cv2.imread('images/opencv.jpeg')

img = np.zeros((400,512,3),np.uint8)
for i in range(255):
    img[:,i]=i
    img[:,256+i] = 255-i

ret, mask=cv2.threshold(img,100,255, cv2.THRESH_BINARY)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('b','image',0,250,nothing)
cv2.createTrackbar('c','image',0,255,nothing)

while(1):
    cv2.imshow('image',mask)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
        
    # get current positions of four trackbars
    b=cv2.getTrackbarPos('b','image')
    c=cv2.getTrackbarPos('c','image')
    ret, mask=cv2.threshold(img,b,c, cv2.THRESH_BINARY)
        
cv2.destroyAllWindows()