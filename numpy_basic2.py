import numpy as np

x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)

print(x)
print()
print(y)
print()
print(x+y)
print()
print(np.add(x,y))  #using add()
print(x-y)
print(x*y)
print()
print(np.multiply(x,y))

#np contains other operations like subraction(),sqrt()

print(np.divide(x,y))
print()
print(x/y)

#transpose of matrix
print(x.T)

print('sum of the elements in the matrix is : ',np.sum(x))
print('sum of the elements in the first row is : ',np.sum(x,axis=0))
print('sum of the elements in the column is is : ',np.sum(x,axis=1))