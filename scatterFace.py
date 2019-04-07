import cv2
import numpy as np

def scatterFace(co , vfaces):
    count=0
    S=np.zeros((1,4096,4096))
    for i in range(len(co)):
        for j in range(int(co[i])):
            temp=vfaces[count]
            temp=temp.reshape(4096,1)
            multiply = np.dot(temp,temp.T)
            S[i]+=multiply
            count+=1
        
        S=np.append(S,np.zeros((1,4096,4096)),axis=0)
    s=np.zeros((4096,4096))
    for i in range(len(S)-1):
        s+=S[i]
    
    return s