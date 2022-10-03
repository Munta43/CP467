import cv2
import numpy as np

img1 = cv2.imread("input1.jpg")
img2 = cv2.imread("input2.jpg")

# # TEST `7`
# using this test case will yield a white window.
# img1 = cv2.imread("house.jpg")
# img2 = cv2.imread("house.jpg")

# The [1::-1]  gets tuples in the order of (width and height).
# By callign .shape we get the height, width and channel in tuples.
# .shape gives row (height), column (width).
img2 = cv2.resize(img2, img1.shape[1::-1])

# Honestly I don't think this is needed because the image does not
# change but if we do have an image that has color, then this would be required.
# Therefore I am thinking we leave it here.
temp1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2GRAY)     # Image 1
temp2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)     # Image 2

# TEST `5`
# might want to keep this to show the different images (idk).
cv2.imshow("temp1", temp1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("temp2", temp2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grabing the hight and width of the images used
# (only need to use 1 image in finding the values as they both are resized to
# be the same dimenions as the other).
imageWidth, imageHeight = temp1.shape

# The image that will be the result of dividing the 2 input images.
divided_img = np.zeros((imageWidth, imageHeight))

# I am going to be dividing image1 by image2 (pixel by pixel).
for i in range(imageWidth):
    for j in range(imageHeight):

        # THIS MIGHT BE INEFFICIENT but gets the job done and removes the error encountered below
        # (without using another library)
        # if temp1[i][j] > 255:
        #     temp1[i][j] = 255
        # if temp1[i][j] < 0:
        #     temp1[i][j] = 0

        # if temp2[i][j] > 255:
        #     temp2[i][j] = 255
        # if temp2[i][j] < 0:
        #     temp2[i][j] = 0

        # NOT DONE YET, NEEDS SOME WORK IN THE WAY THE CALCULATION IS DONE.
        # GETTING ERROR:
        '''RuntimeWarning: invalid value encountered in ubyte_scalars calc = temp1[i][j] / temp2[i][j]'''
        # Might need to use another library to handle extremely huge/small values.
        # ANOTHER THING might be that it is dividing by 0 soooo I need to do something to account for that
        calc = temp1[i][j] / temp2[i][j]

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
