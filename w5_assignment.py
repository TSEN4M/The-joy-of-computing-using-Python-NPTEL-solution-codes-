#week 5 assingnment 2 printing unique elements of a list in sorted order
def uniquE(L):
     ans=[]
     for a in L:
          if L.count(a)==1:
               ans.append(a)
     return sorted(ans)

L=[int(i) for i in input().split()]
print(uniquE(L))

#week 5 assingment 3 printing the first prime number from the list
M=[int(i) for i in input().split()]
def Isprime(num):
     if num<=1:
          return False
     if num==2:
          return True
     for i in range(num-1):
          if num%i==0:
               return False
     return True

for x in M:
     if Isprime(x):
          print(x)
          break
     else:
          continue
          