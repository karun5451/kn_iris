# from numpy import zeros
from skimage.morphology import square, disk, dilation, erosion

def erode(img, size=3):
	selem = disk(int(size))
	gmi = erosion(img, selem)
	# print("shapegmi2",gmi.shape[0],gmi.shape[1])
	return gmi

def dilate(img, size=3):
	selem = disk(int(size))
	gmi = dilation(img, selem)
	# print("shapegmi2",gmi.shape[0],gmi.shape[1])
	return gmi
