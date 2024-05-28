
import string
import random

A=string.ascii_letters
n = int(input())
for i in range(n):
        L=[]
        for j in range(n):
                L.append(random.choice(A))
        for element in L:
                print(element,end='\t')
        print()

#to check unique element from two list
print('Test progrma 2')
L1= ['apple','pine apple','grapes','watermelon','oranges','banana']
L2 =['grapes','cold drink','samosa','oranges','banana']
L=[]
for i in range(len(L1)):
        flag = 0
        for j in range(len(L2)):
                if L1[i]==L2[j]:
                        flag=1
                        break
                else:
                        flag=0
        if flag==0:
                L.append(L1[i])
print(L)

#Print perfect square between 5 to 19
print('Test program 3')
for i in range(5,20):
        if i%5==0:
                print(i**2)

#print all the prime number between the rang of 0-200
print('Test progrma 4')
for i in range(2,101):
        flag=0
        for j in range(2,i):
                if i%j==0:
                        flag=1
                        break
        if flag==0:
                print(i)
#to check if the given number is perfect or not ie, sum of its factor results in the number itself
print('Test program 5')
def perfect_number(num):
        ans=0
        for i in range(1,num):
                if num%i==0:
                        ans=ans+i
        if ans==num:
                print('yes')
                return True
        else:
                return False
perfect_number(6)               #6 is a perfect number

#print a triangle pattern

n=int(input('Enter the row size : '))
for i in range(0,n):
        for j in range(0,n-i-1):
                print(' ',end='')
        for k in range(0,i+1):
                print('*',end='')
        print()

#w4 assignment 2
s=input('Enter a string : ')
vovels = ['A','E','I','O','U','a','e','i','o','u']
cmp = list(s)
ans=[]
for i in range(len(s)):
        if cmp[i] in vovels:
                ans.append(cmp[i])
        else:
                ans.append('_')

print('The ans is :',''.join(str(x) for x in ans))

#to count the number and print if it is exactly present twice
l=input()
temp=list(l)
ans=[]
count=0
for i in range(len(l)):
        count=temp.count(temp[i])
        if count==2 and temp[i] not in ans:
                ans.append(temp[i])
print("the answer is : ", ans)