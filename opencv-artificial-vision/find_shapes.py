# USAGE
# python find_shapes.py --image shapes.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image file")
#args = vars(ap.parse_args())

# load the image
cap = cv2.VideoCapture(0)

while (True):


    _, camcapture = cap.read()
    hsv = cv2.cvtColor(camcapture, cv2.COLOR_BGR2RGB)

    # find all the 'black' shapes in the image
    lower = np.array([0, 0, 0])
    upper = np.array([15, 15, 15])
    shapeMask = cv2.inRange(hsv, lower, upper)

    # find the contours in the mask
    (cnts, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    print "I found %d black shapes" % (len(cnts))
    #cv2.imshow("Mask", shapeMask)

    # loop over the contours
    print len(cnts)
    for c in cnts:
        if cv2.contourArea(c)>800:
            print("Contour found!!!")
            print cv2.contourArea(c)
        # draw the contour and show it
            cv2.drawContours(camcapture, [c], -1, (0, 255, 0), 2)
            cv2.imshow("Image", camcapture)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()