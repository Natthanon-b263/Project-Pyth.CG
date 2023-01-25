import cv2
#การอ่านภาพ
image = cv2.imread("image/programmer.jpg")
print (type(image.ndim))
print (image)