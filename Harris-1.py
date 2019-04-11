import cv2 as cv
import numpy as np

img = cv.imread("E:/OP/chess.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,23,0.04)
img[dst>0.01 * dst.max()] =[0,0,255]
while (True):
    cv.imshow('corners',img)
    if cv.waitKey(50) &0xff ==ord("q"):
        break
cv.destroyAllWindows()