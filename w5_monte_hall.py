import random
doors=[0]*3
goatdoors=[0]*2
swap=0
dont_swap=0
j=0
while(j<5):
     x=random.randint(0,2)    #2 including
     doors[x]='BMW'
     for i in range(3):
          if i==x:
               continue
          else:
               doors[i]='GOAT'
               goatdoors.append(i)
     choice=int(input('Enter the choice for the door 0/1/2 : '))
     door_open=random.choice(goatdoors)
     while door_open==choice:
          door_open=random.choice(goatdoors)
     print("for the hint, one of the goat door is :", door_open)
     ch=input('Now do you want to swap or not y/n : ')
     if ch=='y':
          if doors[choice]=='GOAT':
               print('PLAYER WINS..')
               swap=swap+1
          else:
               print('PLAYER LOST..')
     else:
          if doors[choice]=='GOAT':
               print('PLAYER LOST..')
          else:
               print('PLAYER WINS..')
               dont_swap=dont_swap+1
     j=j+1
print('the wins after swapping is : ', swap)
print('the wins after not swapping : ',dont_swap)