import numpy as np
import cv2
from matplotlib import pyplot as plt
import math


def test(img1, img2):
	MIN_MATCH_COUNT = 5

	# Initiate SIFT detector
	sift = cv2.SIFT()

	# find the keypoints and descriptors with SIFT in both the images
	kp1, des1 = sift.detectAndCompute(img1,None)
	kp2, des2 = sift.detectAndCompute(img2,None)

	FLANN_INDEX_KDTREE = 0 
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)

	flann = cv2.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1,des2,k=2)

	# store all the good matches as per Lowe's ratio test.
	length = 0
	good = []
	for m,n in matches:
		if m.distance < 0.65*n.distance:
		    good.append(m)
	if len(good)>MIN_MATCH_COUNT:
		src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
		dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
		length = length +1
		print dst_pts
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
		matchesMask = mask.ravel().tolist()

		h,w = img1.shape
		pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
		dst = cv2.perspectiveTransform(pts,M)

		img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.CV_AA)

	else:
		print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
		matchesMask = None
		return 0, 0

	sumx = 0
	sumy = 0
	c = 0
	
	#Find the mean point of all the matched points
	for x in dst_pts:
		c = c + 1
	for x in dst_points:
		sumx = sumx + x[0][0]
		sumy = sumy + x[0][1]
	avg_x = sumx/c
	avg_y = sumy/c
	
	#Dimnesions of the input image from the camera
	dim_x = 1280
	dim_y = 720

	#Scaling factor
	KNOWN_DISTANCE = .45
	KNOWN_PIXEL = 106.83 

	#Calculate the x and y distance of the drone from the target
	inches_x = .293*(avg_x - (dim_x/2))/KNOWN_PIXEL
	inches_y = .293*((dim_y/2) - avg_y)/KNOWN_PIXEL

	return (inches_y), inches_x
	
