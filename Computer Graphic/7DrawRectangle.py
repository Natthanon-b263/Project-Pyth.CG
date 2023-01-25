import cv2
#วาดสี่เหลี่ยม
image=cv2.imread("image/programmer.jpg")
imageresize=cv2.resize(image,(500,500))

cv2.rectangle(imageresize,(100,200),(300,400),(0,255,255),10)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(0)
cv2.destroyAllWindows()