'''
CODE IS COPIED FROM ASSIGNMENT 1 AND REUSED FOR CONVOLUTION PART IN A2
'''

import cv2
import numpy as np

# load image, grayscale it and define filter
img = cv2.imread('house.jpg')
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code

img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code

# TEST `1`
# Gives a less clear edge detection compared to the one below.
# filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)

# TEST `2`
# This give a more clear/sharp edge detection.
# filter = np.array([[1, 4, 1], [4, -20, 4], [1, 4, 1]], np.float32)

# TEST `3`
# This is the opposite version of the line above.
# filter = np.array([[-1, -4, -1], [-4, 20, -4], [-1, -4, -1]], np.float32)

# TEST `4`
filter = np.array([[0, -1, 0], [-1, 20, -1], [0, -1, 0]], np.float32)

# calculate the dimention of operation matrix
img_col_num, img_row_num = img.shape
filter_col_num, filter_row_num = filter.shape

# create pallate for new image and adjust to prevent out of bounds error
# THESE WERE + (not -)
y = img_col_num-filter_col_num + 1
x = img_row_num-filter_row_num + 1

filtered_img = np.zeros((y, x))

# iterate pixel by pixel and use convolution to apply the filter
for i in range(y):
    for j in range(x):
        filtered_img[i][j] = np.sum(
            img[i:i+filter_col_num, j:j+filter_row_num]*filter)
        # make sure to check that your pixel values are not above or below the RGB range (0-255)
        if filtered_img[i][j] > 255:
            filtered_img[i][j] = 255
        if filtered_img[i][j] < 0:
            filtered_img[i][j] = 0

    # PROGRAM STATUS INDICATOR
    print("Running!!!")

# PROGRAM STATUS INDICATOR
print("DONE!")

cv2.imshow("Convolution", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code
