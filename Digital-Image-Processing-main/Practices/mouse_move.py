import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        font = cv.FONT_HERSHEY_SIMPLEX
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                cv.putText(img,'[('+str(ix)+','+str(iy)+'),('+str(x)+','+str(y)+')]',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
                cv.putText(img,'[('+str(x)+','+str(y)+')]',(10,500), font, 4,(255,0,0),2,cv.LINE_AA)
        cv.putText(img,'[('+str(x)+','+str(y)+')]',(10,500), font, 1,(0,255,0),1,cv.LINE_AA)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

def draw_text(event,x,y,flags,param):
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,'Mouse Position [('+str(x)+','+str(y)+')]',(10,50), font, 1,(0,255,0),1,cv.LINE_AA)

img = np.zeros((512,812,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_text)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(10) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()