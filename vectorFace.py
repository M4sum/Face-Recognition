import cv2
import numpy as np

def vectorFace(faces):
    vfaces=[]
    
    for i in range(len(faces)):
        vfaces.append(faces[i].ravel())
    
    vfaces=np.array(vfaces)
    
    return vfaces