import random
#print randomized string
w='hello'
ww="".join(random.sample(w,len(w)))
print(ww)

with open('file.txt','r') as myfile: #file open's 2nd argument has w,r for write and read and 'r' for append meaning not overwriting
     x=myfile.read()
     print(x)

sum=0
for i in range(1,3+1):
     for j in range(1,i+1):
          sum+=j
          
print(sum)
n=5
for i in range(1,n):
     for j in range(1,n):
          if j<n-i:
               print(' ',end='')
          else:
               print('*',end='')
     print()

L=[25,23,56,132,456,8,5,2,4,5,67,8,9,3,20,0,0,1,2,5,4,7,8,9,3,1,4,4,2,6,23,53,56,32,35,6]
ans=[]
for i in range(len(L)):
     if L[i] not in ans:
          if L.count(L[i])==2:
               ans.append(L[i])
               print(L[i])

print('testing a[b]')
a=input()
b=5
c=int(a[b])
print(c)