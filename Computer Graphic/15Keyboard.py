import numpy as np, cv2 as cv; cv2=cv

baby ="New Normal";
cv.namedWindow(baby)

image = np.zeros((512,1000,3),np.uint8)

while True:
 
    cv.imshow(baby,image)

    # Keyboard
    code =cv.waitKey(1)
    if code == ord ("Q") :break

    # Change color
    if code == ord ("C"):
       print("COVID-19")
    if code == ord ("1"): 
       image.fill(100)
    if code == ord ("2"):
       image.fill(255)
    if code == ord ("3"):
       image.fill(150)
    if code == ord ("4"):
       image.fill(149)
cv2.destroyAllWindows