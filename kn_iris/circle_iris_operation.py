import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


def adjust_gamma(image, gamma=1.90):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def circle_iris_operation(fname):
    rgb = cv2.imread(fname)
    kernel = np.ones((3,3), np.uint8)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    # gray = cv2.resize(gray1, (200, 240)) 
    # print("gray",gray.size,gray.shape)
    img_blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    vis = gray + img_blackhat
    # vis_resized = cv2.resize(vis, (280, 220)) 
    vis_resized = vis
    vis_median = cv2.medianBlur(vis_resized,3)
    vis_gaussian = cv2.GaussianBlur(vis_median,(3,3),0)

    vis_circles = cv2.HoughCircles(vis_gaussian, cv2.HOUGH_GRADIENT,2.3, 20,minRadius=40,maxRadius=100)
    # final1 = cv2.hconcat([gray,img_blackhat,vis])
    centerx=0
    centery=0
    if vis_circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        vis_circles = np.round(vis_circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
    #     w0,h0 = gray.shape
        output_result=None
        for (x, y, r) in vis_circles:
                mask = np.zeros((gray.shape[0],gray.shape[1]),dtype=np.uint8)   ##
                cv2.circle(mask,(x,y),r,(255,255,255),-1,0,0)                   ##
                result = np.bitwise_and(gray,mask)                              ##
                output_result = result[y-r:y+r,x-r:x+r]   
        output_result_image = output_result
        return output_result_image
    else:
        print("vis_circles not found")




