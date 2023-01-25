import cv2
#กำหนดขนาด
image=cv2.imread("image/programmer.jpg")
imageresize=cv2.resize(image,(500,500))


cv2.circle (imageresize,(250,250),110,(0, 69, 100),4)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(0)
cv2.destroyAllWindows()