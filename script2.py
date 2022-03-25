#Script that resizes all images in a directory to designated resolution.
import glob
import cv2

def imgResize(x, y, c):
    #Get all image from path
    images = glob.glob('*.jpg')

    #Iterate through all image in images
    for image in images:
        #read image and save it to img variable, change 0 to 1 if u want resized img in color
        img = cv2.imread(image, c)
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

h = int(input('Input designated high: '))
w = int(input('Input designated width: '))
color = input('Input 0 for greyscale images or 1 for color images: ')

while color != '1' and color != '0':
    print('Wrong input for colorscale parameter please input 0 or 1 only')
    color = input('Input 0 for greyscale images or 1 for color images: ')
else:
    color = int(color)

imgResize(h, w, color)
