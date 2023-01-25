# การแสดงผลภาพด้วย Matplotlib
import cv2
import matplotlib.pyplot as plt
#การอ่านภาพ
image = cv2.imread("image/programmer.jpg")

#การแสดงภาพ
cv2.imshow("Natthanon",image)
img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()