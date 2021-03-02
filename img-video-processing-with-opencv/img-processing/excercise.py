#Take a list of different images and resize them to  100 X 100 dimentions.
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re_img=cv2.resize(img,(500,500))
    cv2.imshow("New B/W image",re_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, re_img)


