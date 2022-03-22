#Script that resizes all images in a directory to designated resolution.
import glob
import cv2

x = int(input('Input designated high: '))
y = int(input('Input designated width: '))
#Get all image from path
images = glob.glob('*.jpg')

#Iterate through all image in images
for image in images:
    #read image and save it to img variable, change 0 to 1 if u want resized img in color
    img = cv2.imread(image, 0)
    #resize img and save it to resize_image
    resize_image = cv2.resize(img, (y,x))
    #show image on the screen
    cv2.imshow('Hey', resize_image)
    #wait 2 sec
    cv2.waitKey(2000)
    #destroy window
    cv2.destroyAllWindows()
    #save resize_image with 'resized_' adnotation in name
    cv2.imwrite('resized_'+image, resize_image)