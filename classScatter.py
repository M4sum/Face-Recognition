import numpy as np
import cv2

def classScatter(s):
    S=np.zeros((4096,4096))
    for i in range(len(s)):
    
        temp=s[i]
        temp=temp.reshape(4096,1)
        multiply = np.dot(temp,temp.T)
        S+=multiply
        
    
    return 2*S