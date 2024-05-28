import numpy as np

a=np.array([[1,2,3],[3,4,5]])      #list inside list for 2d 
b=np.array([1,2,3])

print(type(a))
print(a.shape)
print(b.shape)

print(b[0],b[1],b[2])
b[1]=6
print(b)

c=np.zeros((3,3))   #making a matrix of zero of 3x3
print(c)

d=np.ones((2,2))    #making a matirx of one of 2x2
print(d)

e=np.full((2,2),6)  #making a matrix of specified number and matrix size
print(e)

f=np.random.random((2,2))     #making a matrix of specified size but random fillings
print(f)

x=np.array([1.003,2])
print(x.dtype)

y=np.array([1,2],dtype=np.int64)
print(y.dtype)