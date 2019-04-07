import cv2
import numpy as np

def averageFace(classes , vfaces):
    j=0
    s=np.zeros((1,4096))
    co=np.zeros(1)

    for i in range(len(classes)):
    
        temp=vfaces[i]
        if(i==0):
            b=classes[i]
            s[0]=temp
            co[j]+=1

        else:
            a=classes[i]
            
            if(b==a):
                s[j]+=temp
                co[j]+=1
            
            else:
                b=a
                j+=1
                s=np.append(s,np.zeros((1,4096)),axis=0)
                co=np.append(co,np.zeros(1))
                s[j]+=temp
                co[j]+=1

    for i in range(len(co)):
        s[i]=s[i]/co[i]
    
    return co , s


    
    
