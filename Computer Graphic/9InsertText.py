import cv2
#การเขียนข้อความ
image=cv2.imread("image/programmer.jpg")
imageresize=cv2.resize(image,(700,500))

#
cv2.putText(imageresize,"NATTHANON",(10,450),cv2.FONT_HERSHEY_SIMPLEX,1.8,(0,255,255),cv2.LINE_8)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()