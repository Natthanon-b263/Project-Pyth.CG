import cv2
import numpy

#กำหนดขนาด
image=cv2.imread("image/programmer.jpg")
#image = numpy.zeros([500,500,3])
points = []

#imageresize=cv2.resize(image,(700,500))

def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),10,(0,255,255),4)       
        points.append((x,y))
        print(points)
        if len(points)>=2:
            #cv2.line(image,points[0],points[1],(255,255,255),5)
            cv2.line(image,points[-2],points[-1],(255,255,255),5)
            #print("[-1]"point)
    cv2.imshow("Natthanon",image)
    
cv2.imshow("Natthanon",image)
cv2.setMouseCallback("Natthanon",clickPosition)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()