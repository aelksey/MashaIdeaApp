import cv2
import threading
import numpy as np
import matplotlib.pyplot as plt
eye_cascade = cv2.CascadeClassifier('haar-cascade-files-master/haarcascade_eye.xml')
face_cascasde = cv2.CascadeClassifier('haar-cascade-files-master/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, frame = cap.read(0)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascasde.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 2)
        roi_gray = gray[y:int((y+h)*0.7), x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            print(eyes)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.circle(roi_color,(int(ex + ew/2),int(ey+eh/2)),5,(0,0,255),-1)
            cv2.putText(roi_color, 'Eye', (ex, ey), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
            if len(eyes)>=2:

                cv2.putText(frame, 'Glasses OFF', (int(x+h/2), y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                linex = []
                liney = []
                widths = []
                heights = []
                for (ex, ey, ew, eh) in eyes:
                    linex.append(ex)
                    liney.append(ey)
                    widths.append(ew)
                    heights.append(eh)
                startx = int(linex[0] + widths[0]/2)
                starty = int(liney[0] + heights[0] / 2)
                finishx = int(linex[1] + widths[1] / 2)
                finishy = int(liney[1] + heights[1] / 2)
                cv2.line(roi_color,(startx,starty),(finishx,finishy),(255,0,0),3)


        cv2.putText(frame, 'Face',(x,y),font, 1,(255,0,0), 2,cv2.LINE_AA)

        print("LitsoNaideno")
    cv2.imshow('videofromwebcam',frame)


    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()