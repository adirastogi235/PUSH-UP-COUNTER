import cv2
import cvzone
from cvzone.PoseModule import PoseDetector
import numpy as np

cap = cv2.VideoCapture(1)

detector = PoseDetector()
per = 0
a1 = 0
color = (0,0,255)
situps = 0
dir = 0
while True:
    __ , img = cap.read()
    #assert isinstance(img, object)

    img = detector.findPose(img)
    lmlist, bbox = detector.findPosition(img,False)
    assert isinstance(lmlist, object)
    if lmlist:
        a1 = detector.findAngle(img,24,26,28)
        per = np.interp(a1,(75,160),(100,0))
        bar_value = np.interp(a1,(75,160),(15,15+300))
        # print(per)
        cv2.rectangle(img,(580,int(bar_value)),(580 + 20,15 + 350),color,cv2.FILLED)
        cv2.rectangle(img,(580,15),(580 + 20,15 + 350),(0,0,0),3)
        cvzone.putTextRect(img,f'{int(per)} %',(575,410),1.2,2,colorT=(),colorR=color,border=3,colorB=())
        if per ==100:
            if dir == 0:
                situps += 0.5
                dir = 1
                color = (0,255,0)
        elif per == 0:
            if dir == 1:
                situps += 0.5
                dir = 0
                color = (0,255,0)
        else:
            color = (0,0,255)
        #print(situps)
        cvzone.putTextRect(img,f'SIT UPS : {str(int(situps))}',(30,30),2,2,colorT=(),colorR=(255,0,0),border=3,colorB=())              
    cv2.imshow('Situps Counter', img)
    if cv2.waitKey(1) == ord('q'):
        break

