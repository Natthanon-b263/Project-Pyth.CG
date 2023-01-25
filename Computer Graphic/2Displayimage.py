import cv2
#กาารอ่านภาพ
image = cv2.imread("image/programmer.jpg")
#กาารแสดงภาพ
cv2.imshow("Natthanon",image)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()
