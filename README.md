# Image_Stiching_for_Panorama
Implementation of SIFT and ORB methods to perform Feature matching between two images and the create a Homography matrix, which can be used to fuse the two images to obtain a larger field of view.
The pairs of input images Ex: foto1A.jpg and foto1B.jpg are slightly images taken from the same camera.

![foto1A](https://user-images.githubusercontent.com/106699115/207804449-929fb313-e8cc-4a72-aa00-b4009149dbe3.jpg)
![foto1B](https://user-images.githubusercontent.com/106699115/207804451-cbcce482-f867-4143-919d-8ba380446574.jpg)

 These images are combined to give:
 
 ![foto1](https://user-images.githubusercontent.com/106699115/207804558-10a98d3c-7639-48f1-ba72-bebd1e1572f2.png)

# RANSAC Regressor

Implementation of Random Sample Consensus Algorithm using python to regress a best fit line which has least distances from points or blobs in an image using OpenCV.

# Sample image

![line_ransac](https://user-images.githubusercontent.com/106699115/207798180-2e944318-3879-4875-bdd8-b1f9fd7a9cfa.png)


# Output image with best-fit line

![found_linw_2](https://user-images.githubusercontent.com/106699115/207798195-69e53c7c-f98a-432d-b013-79139b54a62b.png)
