import cv2
from PIL import Image

img=Image.open('C:/Users/death/Downloads/python/image_processing.jpg')

#mirror image is in matrix can be caled transposed

transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save('C:/Users/death/Downloads/python/transposed.jpg')
print('Done Flipping ')



#Image enhancement
# we will use CLAHE (contrast limiter adaptive histogram equilizaition)

img=cv2.imread('C:/Users/death/Downloads/python/image_processing.jpg')

#preparation for CLAHE
clahe=cv2.createCLAHE()

#converting to gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply enhancement
enh_img=clahe.apply(gray_img)

#save it to a file
cv2.imwrite('C:/Users/death/Downloads/python/enhanced.jpg',enh_img)
print('DONE ENHANCING')