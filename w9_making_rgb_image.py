import numpy as np
from PIL import Image

width=2
height=2

array=np.zeros([height,width,3],dtype=np.uint8)   #uint=unsigned int

img=Image.fromarray(array)

img.save('W9_test.png')

array1=np.zeros([100,200,3],dtype=np.uint8)  #100,200,3 is the height width values and 3 as in rgb
array1[:,:100]=[255,128,0]   #orange color
array1[:,100:]=[0,0,255] #blue color

img=Image.fromarray(array1)
img.save('w9_test2.png')