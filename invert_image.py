import cv2

img = cv2.imread("camaleon.png",cv2.IMREAD_UNCHANGED)

img = img[::-1,::-1,:]

cv2.imwrite("output.png",img)