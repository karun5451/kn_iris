from kn_iris.morph import *
import numpy as np
def pupil_detect(img): 
	pupil=np.where((img<50) & (img>3),1.,0.)
	pupil=erode(pupil,4)
	pupil=dilate(pupil,2) 
	return pupil
