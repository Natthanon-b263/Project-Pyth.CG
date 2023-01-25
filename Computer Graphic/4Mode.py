import cv2
#กำหนดรูปแบบภาพ
#image=cv2.imread("image/programmer.jpg",0)
image=cv2.imread("image/programmer.jpg",1)
imageresize=cv2.resize(image,(500,500))
cv2.imshow("Natthanon",imageresize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()