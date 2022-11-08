# DIVISION
import cv2
import numpy as np

img1 = cv2.imread("input1.jpg")
img2 = cv2.imread("input2.jpg")

# The [1::-1]  gets tuples in the order of (width and height).By calling .shape we get the height,
# width and channel in tuples.
img2 = cv2.resize(img2, img1.shape[1::-1])
# Change the image to a grayscaled image.
img1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)     # Image 1
img2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)     # Image 2

# Display images.
cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Image 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grabing the hight and width of the images used (only need to use 1 image in finding the values as
# they both are resized to be the same dimenions as the other).
imageWidth, imageHeight = img1.shape
# The image that will be the result of dividing the 2 input images.
divided_img = np.zeros((imageWidth, imageHeight))

# We will be dividing image1 by image2 (pixel by pixel).
for i in range(imageWidth):
    for j in range(imageHeight):
        # A check for the value of the pixel to avoid division by 0
        if (img2[i][j] == 0):
            calc = 0
        else:
            calc = img1[i][j] / img2[i][j]
        if calc > 255:
            calc = 255
        if calc < 0:
            calc = 0
        divided_img[i][j] = calc
    # PROGRAM STATUS INDICATOR
    print("Running!!!")

# Display processed image.
cv2.imshow("Divided Image", divided_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# PROGRAM STATUS INDICATOR
print("DONE!")


# CONVOLUTION
'''
CODE IS COPIED FROM ASSIGNMENT 1 AND REUSED FOR CONVOLUTION PART IN A2
'''
import cv2
import numpy as np

# Load image and display it.
img = cv2.imread('house.jpg')
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code
# Change image to grayscale and then display it.
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code

# Filter being use.
filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)

# calculate the dimention of operation matrix
img_col_num, img_row_num = img.shape
filter_col_num, filter_row_num = filter.shape
y = img_col_num-filter_col_num + 1
x = img_row_num-filter_row_num + 1

# Create a holder for processed image.
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

for i in range(y):
    for j in range(x):
        # Re-writing the original image.
        img[i][j] = img[i][j] + filtered_img[i][j]
    # PROGRAM STATUS INDICATOR
    print("Running!!!")

# PROGRAM STATUS INDICATOR
print("DONE!")

cv2.imshow("test", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Diplay processed image.
cv2.imshow("Convolution", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # if you press enter on the img you can proceed with the code
