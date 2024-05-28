import imageio 
from PIL import Image
import numpy as np
import random

img=imageio.imread('C:/Users/death/Downloads/python/map.png')

count_pun=0
count_in=0
count=0

while(count<100000):
     x=random.randint(0,686)       #x acts as the vertical value and y as horizontal value
     y=random.randint(0,644)       #x & y are reversed
     z=0
     if img[x][y][z]==61:               #x=height y=width 
          count_in+=1
          count+=1
     elif img[x][y][z]==80:
          count_pun+=1
          count+=1

area_pun=(count_pun/count_in)*3287263
print('The area of punjab is approximately : ' ,area_pun)