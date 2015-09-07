__author__ = 'hcadavid'

from PIL import Image

import cv
import cv2
import glyphDec as gd

cap = cv2.VideoCapture(0)
#capture = cv.CaptureFromCAM(0)



while(1):

    _, frame = cap.read()

    grid = gd.glyphRec(cv.fromarray(frame))

    cv2.imshow('frame',frame)

    print grid

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()