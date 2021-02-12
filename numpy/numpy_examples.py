import numpy
import cv2

#Generates the array using numpy.
n=numpy.arange(27)
print(n)

#Generates the 3D array and prints it.
print(n.reshape(3,3,3))

#Reads the image and print in array format.
img = cv2.imread("smallgray.png",0)
print(img)

#Writes to file, i.e creates new image.
cv2.imwrite("newimage.png", img)

#Slicing and iterating through arrays
print(img[0:2,2:4])

#Access array row by row.
for rows in img:
    print(rows)

#Access perticular element. Prints 3rd row and 5th element.
#Index starts at 0 so that difference is in the positions.
print(img[2,4])

#To concatinate the 2 arrays horizontally.
imghr=numpy.hstack((img, img))
print(imghr)

#To concatenate the 2 arrays vertically.
imgvr=numpy.vstack((img, img))
print(imgvr)

#Spilts the array horizontally. 2 is no of splits.
splithr=numpy.hsplit(imghr,2)
print(splithr)

#Splits the array vertically.
splitvr=numpy.vsplit(imghr,3)
print(splitvr)