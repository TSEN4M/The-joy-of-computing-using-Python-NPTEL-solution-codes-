# 3n+1 problem
def checkNum(num):
     iterations=1
     while num!=1:
          if num%2==0:
               num=int(num/2)
               print(num,iterations)
          else:
               num=3*num+1
               print(num,iterations)
          iterations+=1
     #print(num,iterations)

checkNum(254)