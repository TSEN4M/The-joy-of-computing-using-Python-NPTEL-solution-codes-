sol=[]
def shift(N):
     x=len(N)
     print(x)
     for i in range(x):
          print(N[i])
          if N[i]==0:
               print('equal to 0')
               pos=x-i-1
               print('position',pos)
               sol.insert(pos,N[i])
          else:
               print('not equal to 0')
               sol.insert(i,N[i])
     print(sol)
N=[0,1,0,2,3,4,0,5]
shift(N)