from kn_iris.morph import *
import numpy as np
def iris_detect(img):
	iris=np.where((img>50) & (img < 120),1.,0.)
	iris = dilate(iris,4)
	iris = erode(iris,2) 	
	return iris
