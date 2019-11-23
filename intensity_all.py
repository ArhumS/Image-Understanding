import glob
import cv2
import sys
import os
import math
import numpy as np

limages=sorted(glob.glob('x5l/left*.ppm'))
lengthl=len(limages)
img = []
name=1 #Counter to write labels
for I in range (0,lengthl) :
    name+=1 
    print('image to process',I)
    image  = cv2.imread(limages[I])
    blur_cur = cv2.GaussianBlur(image,(3,3),0)
    blur_nxt = cv2.GaussianBlur(image + 1,(3,3),0)
    img.append (blur_cur)
    cv2.imshow('lefts only...', image)
    cv2.waitKey(500)
    
    print('img shape:', np.array(image).shape)
    print('Main Loop')
    
    (row, col,_) = image.shape
    print image[0]
    print "blur_cur", blur_cur.shape
    print blur_cur[0]
    
#Colour assignment
    white_px = np.asarray([142, 142, 142]) # Threshold
    orange_px = np.asarray([0, 165, 255]) # R=255, G=165, B=0.,pink = 255,20,147
    
# Part - 1 # Intensity label
    for r in range(row):
        for c in range(col):
		if (blur_cur[r][c][0] >= white_px[2] and blur_cur[r][c][1] >= white_px[1] and blur_cur[r][c][2] >= white_px[0] ):
	    		blur_cur[r][c] = orange_px
    cv2.imwrite(str(name) +'~/intall/intall.png', blur_cur)
# Part - 2 # Difference label - and
# Part - 3 # Both classes ANDED - coming up next
