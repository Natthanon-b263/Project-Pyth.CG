from traceback import FrameSummary
import cv2
 
cap = cv2.VideoCapture("image/Natthanon126-4.mp4")

while (True):
    check , frame = cap.read() #รับภาพจากกล้อง
    
    if check == True :
      #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      #cv2.imshow("Present Introduction Natthanon",gray)
      cv2.imshow("Present Introduction Natthanon",frame)
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
    else :
        cv2.destroyAllWindows()
        break
cap.release()
cv2.waitKey(0)