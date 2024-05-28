from PIL import Image

img=Image.open('w9_test2.png')

rgb_img=img.convert('RGB')         #convert the image to RGB values as into a matrix

r,g,b=rgb_img.getpixel((150,1))      #will fetch rgb values at the specified position

print(r,g,b)
