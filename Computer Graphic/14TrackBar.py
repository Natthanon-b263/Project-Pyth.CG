import cv2
import numpy as np
image=np.zeros((300,500,3),np.uint8)

cv2.namedWindow("Computer Graphic Trackbar")

def output(value):
    #print(value)
    pass
cv2.createTrackbar("BLUE","Computer Graphic Trackbar",0,255,output)
cv2.createTrackbar("GREEN","Computer Graphic Trackbar",0,255,output)
cv2.createTrackbar("RED","Computer Graphic Trackbar",0,255,output)

while True:
   cv2.imshow("Computer Graphic Trackbar",image)
   if cv2.waitKey(1) & 0xFF == ord("e"):
      break
   blue = cv2.getTrackbarPos("BLUE","Computer Graphic Trackbar")
   green = cv2.getTrackbarPos("GREEN","Computer Graphic Trackbar")
   red = cv2.getTrackbarPos("RED","Computer Graphic Trackbar")
   image[:] = [blue,green,red]

   cv2.imshow("Computer Graphics",image)
   cv2.waitKey(delay=0)
   cv2.destroyAllWindows()