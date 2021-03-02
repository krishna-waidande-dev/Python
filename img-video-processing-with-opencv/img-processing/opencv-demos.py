import cv2

#For black and white pass 0. For Reading image as it is pass 1.
#How to load image in Python.
img=cv2.imread("galaxy.jpg", 0)

print(type(img))

print(img)

#How much pixels are there in numpy array.
print(img.shape)

#Tells how much dimentions array is.
print(img.ndim)

#Resize image.
resize_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

#To write the image in file.
cv2.imwrite("Galaxy_resized.jpg", resize_image)

#To display image in window.
cv2.imshow("Galaxy", resize_image)

#0  is passed to freeze the image window and if we click any key then window will be closed.
cv2.waitKey(0)
cv2.destroyAllWindows()

