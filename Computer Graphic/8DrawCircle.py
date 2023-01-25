import cv2
#การอ่านภาพ
image = cv2.imread("image/programmer.jpg")

#การกำหนดขนาดภาพ
imageresize=cv2.resize(image,(500,500))

#การวาดวงกลม
cv2.circle(imageresize,(250,250),250,(0,0,255),10)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(delay=9000)
cv2.destroyAllWindows()