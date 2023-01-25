import cv2
#กำหนดขนาด
image=cv2.imread("image/programmer.jpg",0)
imageresize=cv2.resize(image,(500,500))
cv2.imshow("Natthanon",imageresize)
cv2.imwrite("programmerNEW.jpg",imageresize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()