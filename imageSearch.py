import glob
import cv2
import numpy as np
import re

def imgageSearch(address):
    img_name=glob.glob(str(address))

    class_name=[]

    pattern=re.compile(r'16BIT\d\d\d')

    for i in range(len(img_name)):
        match=re.findall(pattern,img_name[i])
        class_name.append(match)
        
    class_name=np.array(class_name)
    totalNoOfImages=len(img_name)
    class_name=class_name.reshape(totalNoOfImages,)
    img=[]

    for i in img_name:
        c=cv2.imread(i,0)
        img.append(c)
    img=np.array(img)

    return class_name , img