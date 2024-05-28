import random
import matplotlib.pyplot as plt

account=0

x=[]
y=[]

for i in range(365):
     x.append(i+1)
     bet=random.randint(1,10)
     lucky_draw=random.randint(1,10)
     #print('BET :',bet)
     #print('LUCKY DRAW :',lucky_draw)
     if bet==lucky_draw:
          print('YOU WON')
          account+=900
     else:
          print('YOU LOST')
          account-=100
     y.append(account)
     
plt.plot(x,y)
plt.show()

print('YOU GOT : ',account)