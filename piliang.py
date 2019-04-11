import os.path
import cv2 as cv
import glob


def convertjpg(jpgfile,outdir,width=128,height=128):

    src = cv.imread(jpgfile,cv.IMREAD_ANYCOLOR)

    try :
        dst =cv.resize(src,(width,height),interpolation=cv.INTER_CUBIC)


