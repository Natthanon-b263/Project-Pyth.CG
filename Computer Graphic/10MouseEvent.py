import cv2
#กำหนดขนาด
image=cv2.imread("image/programmer.jpg")

imageresize=cv2.resize(image,(500,500))

def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
       text = str(x)+","+str(y)
       cv2.putText(imageresize,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),cv2.LINE_4)
       #cv2.putText(imageresize,"COVID",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),cv2.LINE_4)
       cv2.imshow("Natthanon",imageresize)

cv2.imshow("Natthanon",imageresize)

cv2.setMouseCallback("Natthanon",clickPosition)

cv2.waitKey(delay=0)
cv2.destroyAllWindows()