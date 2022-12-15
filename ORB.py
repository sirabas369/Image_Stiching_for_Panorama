import cv2
import numpy as np

img1 = cv2.imread('/home/sirabas/Documents/AGV/Stiching/panorama/foto5B.jpg')
img2 = cv2.imread('/home/sirabas/Documents/AGV/Stiching/panorama/foto5A.jpg')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kps1, features1 = orb.detectAndCompute(gray1, None)
kps2, features2 = orb.detectAndCompute(gray2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck = True)
matches = bf.match(features1, features2)
matches = sorted(matches, key = lambda x:x.distance)


img3 = cv2.drawMatches(img1, kps1, img2, kps2, matches[:50], img2, flags=2)

kps1_pt = np.float32([ kp.pt for kp in kps1])
kps2_pt = np.float32([ kp.pt for kp in kps2])

pts1 = np.float32([kps1_pt[m.queryIdx] for m in matches])
pts2 = np.float32([kps2_pt[m.trainIdx] for m in matches])

(h, status) = cv2.findHomography(pts2, pts1, cv2.RANSAC, ransacReprojThreshold = 4)

width = img2.shape[1] + img1.shape[1]
height = img2.shape[0] + img1.shape[0]

result = cv2.warpPerspective(img2, h, (width, height))

result[0:img1.shape[0], 0:img1.shape[1]] = img1

graycrop = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
threshcrop = cv2.threshold(graycrop, 0, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(threshcrop.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0]

# get the maximum contour area
c = max(cnts, key=cv2.contourArea)

# get a bbox from the contour area
(x, y, w, h) = cv2.boundingRect(c)

# crop the image to the bbox coordinates
result = result[y:y + h, x:x + w]

cv2.namedWindow('feature mapping', cv2.WINDOW_NORMAL)
cv2.imshow('feature mapping', img3)

cv2.namedWindow('output', cv2.WINDOW_NORMAL)
cv2.imshow('output', result)

cv2.imwrite("foto5.png",result)

cv2.waitKey(0)

