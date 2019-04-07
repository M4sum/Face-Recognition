import cv2
import numpy as np

def eigenFace(vfaces):
    cov=np.dot(vfaces,vfaces.T)

    wev,vev=np.linalg.eig(cov)
    
    U=np.dot(vfaces.T,vev)

    return U