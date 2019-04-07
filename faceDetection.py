import cv2
import numpy as np

def faceDetection(class_name, img):
    face_cascade = cv2.CascadeClassifier('C:/Users/ALL/AppData/Local/Programs/Python/Python37/Scripts/haarcascade_frontalface_default.xml')
    faces=[]
    classes=[]

    for i in range(len(img)):
        t=face_cascade.detectMultiScale(img[i], 1.2, 5)
        if type(t) != tuple:
            if t.shape != (1,4):
                (x,y,h,w) = t[0]
                faces.append(img[i][y:y+w , x:x+h])
                classes.append(class_name[i])
            if t.shape == (1,4):
                for (x,y,h,w) in t:
                    faces.append(img[i][y:y+w , x:x+h])
                    classes.append(class_name[i])
    faces=np.array(faces)
    classes=np.array(classes)


    for i in range(len(faces)):
        faces[i]=cv2.resize(faces[i],(64,64))
    
    return classes , faces