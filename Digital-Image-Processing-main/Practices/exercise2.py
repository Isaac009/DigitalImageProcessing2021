import cv2
import matplotlib.pyplot as plt
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)

# cv2.namedWindow('image')

# # create trackbars for color change
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)

# # create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image',0,1,nothing)

# while(1):
#     cv2.imshow('image',img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     s = cv2.getTrackbarPos(switch,'image')
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]

# cv2.destroyAllWindows()

# img1 = cv2.imread('images/bowlboy.jpeg')
# img2 = cv2.imread('images/opencv.jpeg')
# dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture('tracking4.avi')
frame_counter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame_counter += 1
    #If the last frame is reached, reset the capture and the frame_counter
    # if frame_counter == cap.get(cv2.CV_CAP_PROP_FRAME_COUNT):
    #     frame_counter = 0 #Or whatever as long as it is the same as next line
    #     cap.set(cv2.CV_CAP_PROP_POS_FRAMES, 0)
    # print(ret)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of green color in HSV
    lower_gr = np.array([10,45,70])
    upper_gr = np.array([60,255,255])
    # lower_gr = np.array([6,24,57])
    # upper_gr = np.array([44,255,255])
    # lower_gr = np.array([60,100,100])
    # upper_gr = np.array([255,255,0])
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_gr, upper_gr)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xFF #== ord('q'):
    if k == 27:
        break
    if not ret:
        cap.release()
cv2.destroyAllWindows()