from imageSearch import imgageSearch
from faceDetection import faceDetection
from vectorFace import vectorFace
from eigenFace import eigenFace
from averageFace import averageFace
from scatterFace import scatterFace
from classScatter import classScatter
import numpy as np
import cv2

address='C:/Users/All/Desktop/database/*.*'

class_name , img = imgageSearch(address)

classes , faces = faceDetection(class_name,img)

vfaces = vectorFace(faces)

eigenface = eigenFace(vfaces)

co , avgface=averageFace(classes,vfaces) 

scatface = scatterFace(co , vfaces)

classcat = classScatter(avgface)


