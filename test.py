n=int(input())
sol=[]
for i in range(1,n+1):
  for j in range(2,n+1-i):
    if i%j==0 and i!=j and i!=n:
      break
    else:
      sol.append(i)
for i in range(len(sol)-2):
  if sol[i]==sol[i+1]-1 or sol[i+1]-2:
    print(sol[i],sol[i+1])
      