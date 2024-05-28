L=["Practice","makes","the","man","percect"]
L.sort()
for elements in L:
    print(elements)
    
for i in range(1,11):
    if(i%2==0):
        print(i)
    
import random

M=[]
for i in range(10):
    M.append(random.randint(0,10))
M.sort()
M.reverse()
print(M)
