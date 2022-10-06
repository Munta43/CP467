import cv2
import numpy as np

img1 = cv2.imread("input1.jpg")
img2 = cv2.imread("input2.jpg")

# The [1::-1]  gets tuples in the order of (width and height).
# By callign .shape we get the height, width and channel in tuples.
# .shape gives row (height), column (width).
img2 = cv2.resize(img2, img1.shape[1::-1])

# Honestly I don't think this is needed because the image does not
# change but if we do have an image that has color, then this would be required.
# Therefore I am thinking we leave it here.
img1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)     # Image 1
img2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)     # Image 2

cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grabing the hight and width of the images used
# (only need to use 1 image in finding the values as they both are resized to
# be the same dimenions as the other).
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

cv2.imshow("Divided Image", divided_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# PROGRAM STATUS INDICATOR
print("DONE!")
