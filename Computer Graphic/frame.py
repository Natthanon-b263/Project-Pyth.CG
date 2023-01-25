import cv2
#การอ่านภาพ
image = cv2.imread("image/programmer.jpg")

#การกำหนดขนาดภาพ
imageresize=cv2.resize(image,(500,500))


cv2.rectangle(imageresize,(500,0),(0,500),(255,0,255),30)
cv2.line(imageresize,(0,0),(500,0),(255,0,0),30)
cv2.line(imageresize,(0,0),(0,500),(0,255,0),30)

cv2.imshow("Natthanon",imageresize)
cv2.waitKey(delay=9000)
cv2.destroyAllWindows()