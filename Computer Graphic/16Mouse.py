import numpy as np, cv2 as cv; cv2=cv
root_mouse = ("Natthanon Bunthao");
cv.namedWindow(root_mouse)
def on_mouse_event(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        ...
    if event == cv.EVENT_LBUTTONUP:
        ...
    if event == cv.EVENT_RBUTTONUP:
        ...
    if event == cv.EVENT_MBUTTONUP:
        ...
    if event == cv.EVENT_MBUTTONUP and flags == cv.EVENT_FLAG_SHIFTKEY:
        ...
    if event == cv.EVENT_MBUTTONUP and flags == cv.EVENT_FLAG_SHIFTKEY | cv.EVENT_FLAG_CTRLKEY:
        ...
    # Event_LBUTTON
    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        print('click L, ' + str([x, y]))
        cv.circle(image,(x,y),5,(0,255,255),1)

    # Mouse moves
    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON | cv.EVENT_FLAG_SHIFTKEY:
        print('click L, ' + str([x, y]))
        cv.circle(image,(x-10,y+10),25,(155,0,0),1)
        cv.circle(image,(x+10,y-10),25,(155,0,0),1)
        cv.circle(image,(x-10,y-10),25,(155,0,0),1)
        cv.circle(image,(x+10,y+10),25,(155,0,0),1)
    
    # when shift is pressed
    if flags == cv.EVENT_FLAG_SHIFTKEY:
        cv.circle(image,(x,y),150,(155,0,0),1)
    
    # click mouse button
    if event == cv.EVENT_MBUTTONUP:
        print('click M, ' + str([x, y]))
        a_line_height = 8
        a_color = (250, 0, 149)
        cv.rectangle(image, (x-30,y-30), (x+30,y+30), a_color, a_line_height)

cv.setMouseCallback(root_mouse, on_mouse_event)
# Create image
image = np.ones((500,1000,3), np.uint8)
while True:
    cv.imshow(root_mouse, image)
    code = cv.waitKey(1)
    if code == ord('q'):
        break
cv.destroyAllWindows()