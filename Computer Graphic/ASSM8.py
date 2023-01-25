import numpy as np, cv2 as cv; cv2=cv
cv2.namedWindow("STUDENT RMUTP")
baby ="STUDENT RMUTP";
image = np.zeros((400,400,3),np.uint8)
while True:
    cv.imshow(baby,image)

    # Keyboard
    code =cv.waitKey(1)
    if code == ord ("Q") :break

    # Change color
    if code == ord ("N"):
       print("Natthanon")
    if code == ord ("1"): 
       image.fill(100)
    if code == ord ("2"):
       image.fill(255)
    if code == ord ("3"):
       image.fill(150)
    if code == ord ("4"):
       image.fill(149)

image=cv2.imread("image/Natthanon.jpg")
imageresize=cv2.resize(image,(500,500))
points = []
def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),5,(0,255,255),3)       
        points.append((x,y))
        print(points)
        if len(points)>=2:
            #cv2.line(image,points[0],points[1],(255,255,255),5)
            cv2.line(image,points[-2],points[-1],(255,255,255),5)
            #print("[-1]"point)
    cv2.imshow("Natthanon",image)
    
cv2.imshow("Natthanon",image)
cv2.setMouseCallback("Natthanon",clickPosition)
cv2.waitKey(delay=0)
#image = numpy.zeros([500,500,3])
points = []

#imageresize=cv2.resize(image,(700,500))

def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),10,(0,255,255),4)       
        points.append((x,y))
        print(points)
        if len(points)>=2:
            #cv2.line(image,points[0],points[1],(255,255,255),5)
            cv2.line(image,points[-2],points[-1],(255,255,255),5)
            #print("[-1]"point)
cv2.imshow("Natthanon",image)
cv2.setMouseCallback("Natthanon",clickPosition)
cv2.waitKey(delay=0)


cv2.namedWindow("Computer Graphic Trackbar")
def clickPosition(event,x,y,flages,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),10,(0,255,255),4)       
        points.append((x,y))
        print(points)
        if len(points)>=2:
            #cv2.line(image,points[0],points[1],(255,255,255),5)
            cv2.line(image,points[-2],points[-1],(255,255,255),5)
            #print("[-1]"point)
    cv2.imshow("Natthanon",image)
    cv2.setMouseCallback("Natthanon",clickPosition)

def output(value):
    #print(value)
    pass
cv2.createTrackbar("BLUE","Computer Graphic Trackbar",0,255,output)
cv2.createTrackbar("GREEN","Computer Graphic Trackbar",0,255,output)
cv2.createTrackbar("RED","Computer Graphic Trackbar",0,255,output)

while True:
   cv2.imshow("Computer Graphic Trackbar",image)
   if cv2.waitKey(1) & 0xFF == ord("e"):
      break
   blue = cv2.getTrackbarPos("BLUE","Computer Graphic Trackbar")
   green = cv2.getTrackbarPos("GREEN","Computer Graphic Trackbar")
   red = cv2.getTrackbarPos("RED","Computer Graphic Trackbar")
   image[:] = [blue,green,red]
   cv2.destroyAllWindows
