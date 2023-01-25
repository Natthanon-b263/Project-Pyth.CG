import cv2
#img = cv2.imread("image/programmer.jpg",0)
img = cv2.imread("image/programmer.jpg",1)

edg = cv2.Laplacian(img,-1)
cv2.imshow("Original",img)
cv2.imshow("Edge",edg)
cv2.waitKey(0)
cv2.destroyAllWindows()