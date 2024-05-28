import numpy 
from PIL import Image

im=Image.open('C:/Users/death/Downloads/python/jisoo.jpeg')

pixelMap=im.load()  #load the image in a variable

#im.show()

I=numpy.asanyarray(Image.open('C:/Users/death/Downloads/python/jisoo.jpeg'))
print(I) 

#creating the compressed image as img
img=Image.new(im.mode,im.size)
pixelNew=img.load()

'''
the image has 8 bit and so we reduce it to 3 bit as
0-31 we will put 0
32-63 we will put 1
64-95 we will put 2
96-127 we will put 3
128-159 we will put 4
160-191 we will put 5
192-223 we will put 6
224=255 we will put 7
'''

for i in range(img.size[0]):  #0 as in row
     for j in range(img.size[1]):
          if pixelMap[i,j]>=0 and pixelMap[i,j]<=31:
               pixelNew[i,j]=0
          elif pixelMap[i,j]>=32 and pixelMap[i,j]<=63:
               pixelNew[i,j]=1
          elif pixelMap[i,j]>=64 and pixelMap[i,j]<=95:
               pixelNew[i,j]=2
          elif pixelMap[i,j]>=96 and pixelMap[i,j]<=127:
               pixelNew[i,j]=3
          elif pixelMap[i,j]>=128 and pixelMap[i,j]<=159:
               pixelNew[i,j]=4
          elif pixelMap[i,j]>=160 and pixelMap[i,j]<=191:
               pixelNew[i,j]=5
          elif pixelMap[i,j]>=192 and pixelMap[i,j]<=223:
               pixelNew[i,j]=6
          elif pixelMap[i,j]>=224 and pixelMap[i,j]<=255:
               pixelNew[i,j]=7
               
img.save('C:/Users/death/Downloads/python/jisoo2.jpeg')
J=numpy.asanyarray(Image.open('C:/Users/death/Downloads/python/jisoo2.jpeg'))
print(J)