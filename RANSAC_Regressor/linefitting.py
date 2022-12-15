import cv2
import sys
from cv2 import WINDOW_NORMAL
import numpy as np

img = cv2.imread('/home/sirabas/Documents/AGV/Stiching/line fitting/line_ransac.png')
orig = np.copy(img)

# convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

sample_space = []

circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 3,param1=100, param2=6, minRadius=4, maxRadius=7)

if circles is not None:
    for i in circles[0, :]:
        sample_space.append([ int(np.around(i[0])), int(np.around(i[1])) ])
        cv2.circle(orig, (int(np.around(i[0])), int(np.around(i[1]))), 1, (0, 0, 255), 0)


def find_model(p1, p2):
    # we just add some noise to avoid division by zero
    [x1, y1] = p1
    [x2, y2] = p2
    
    slope = (y2 - y1) / (x2 - x1 + sys.float_info.epsilon)
    intercept = y2 - slope * x2
 
    return (slope, intercept)

def perp_dist(m , c, x , y):
 
    num = np.abs(y - m*x - c)
    denom = np.sqrt(1 + m**2)

    dist = num/denom
 
    return dist

max_inliers = 0
best_fit = [[0,0] ,[0,0] , [0]]

for i in range(1000):
    np.random.shuffle(sample_space)
    pt1 = sample_space[0]
    pt2 = sample_space[1]
    test_points = sample_space[2:]
    m , c = find_model(pt1, pt2)
    inlier = 0
    for j in range(len(test_points)):
        dist = perp_dist(m, c, test_points[j][0] , test_points[j][1])
        if (dist < 20):
            inlier += 1

    if(inlier > max_inliers):
        max_inliers = inlier
        best_fit = [np.copy(pt1) , np.copy(pt2) , [np.copy(m), np.copy(c)]]


cv2.line(orig , (best_fit[0][0], best_fit[0][1]), (best_fit[1][0], best_fit[1][1]) ,(0,0,255), 2)
print(0, best_fit[2][1],  int((-1)*best_fit[2][1]/best_fit[2][0]) , 0)
cv2.line(orig , (0, int(best_fit[2][1])), ( int((-1)*best_fit[2][1]/best_fit[2][0]) , 0) ,(0,255,0), 2)
print(len(sample_space))
print(max_inliers)

cv2.namedWindow('found line', WINDOW_NORMAL)
cv2.imshow('found line',  orig)
cv2.namedWindow('img', WINDOW_NORMAL)
cv2.imshow('img',  img)
cv2.waitKey(0)