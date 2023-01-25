import cv2
#วาดเส้นตรง
image=cv2.imread("image/programmer.jpg")
imageresize=cv2.resize(image,(500,500))

cv2.line(imageresize,(0,0),(500,0),(255,0,0),20)
cv2.arrowedLine(imageresize,(0,500),(0,0),(255,255,255),20)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()