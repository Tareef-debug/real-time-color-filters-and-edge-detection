import cv2
import numpy as np
cam=cv2.VideoCapture(0)
print("""Keyboard Controls:
b-Blue tint
r-red  tint
g= green tint
x- GAussian Blur
m-median filter
l-laplacian edge detection
s-soble edge detection
c-canny edge detection
q-quit"""
)
mode="n"
while True:
    success,frame=cam.read()
    if not success:
        print("Could not read frames")
        break
    output=frame.copy()
    if mode=="b":
        output[:,:,1]=0
        output[:,:,2]=0
    if mode =="g":
        output[:,:,0]=0
        output[:,:,2]=0
    if mode=="r":
        output[:,:,1]=0
        output[:,:,0]=0
    if mode=="x":
        output=cv2.GaussianBlur(frame,(15,15),0)
    if mode=="m":
        output=cv2.medianBlur(frame,15)
        if mode=="s":
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
            sobelx=cv2.Sobel(gray,cv2.CV64F,1,0,ksize=3)
            output=cv2.magnitude(sobelx,sobely)
            output=np.uint8(output)
        if mode=="l":
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            output=cv2.Laplacian(gray,cv2.CV_64F)
            output=np.uint(np.absolute(output))
        if mode=="c":
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            output=cv2.Canny(gray,100,200)
        cv2.imshow("Final Results",output)
        keys=cv2.waitKey==(1) & 0XFF
        if keys==ord("b"):
            mode="b"
        if keys==ord("r"):
            mode="r"
        if keys==ord("g"):
            mode="g"
        if keys==ord("c"):
            mode="c"
        if keys==ord("x"):
            mode="x"
        if keys==ord("l"):
            mode="l"
        if keys==ord("s"):
            mode="s"
        if keys==ord("q"):
            break
cam.release()
cv2.destroyAllWindows()
