import cv2
import numpy

#กำหนดขนาด
image=cv2.imread("image/programmer.jpg")

imageresize=cv2.resize(image,(700,500))

def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
       blue = imageresize[y,x,0]
       green = imageresize[y,x,1]
       red = imageresize[y,x,2]
       imgcolor=numpy.zeros([300,300,3],numpy.uint8)
       imgcolor[:]=[blue,green,red]

       cv2.imshow("RessultProgrammer",imgcolor)


cv2.imshow("Natthanon",imageresize)
cv2.setMouseCallback("Natthanon",clickPosition)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()