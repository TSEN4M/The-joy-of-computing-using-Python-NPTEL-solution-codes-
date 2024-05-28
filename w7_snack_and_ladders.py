import random
from PIL import Image
end=100

def show_board():
     img=Image.open('C:/Users/death/Downloads/slb.jpg')
     img.show()

def check_ladder(points):
     ladder={8:26,21:82,43:77,50:91,21:82,54:93,62:96,66:87,80:100}
     if points in ladder.keys():
          print('LADDER')
          return ladder[points]
     else:
          return points

def check_snakes(points):
     snakes={44:22,46:5,48:9,52:11,55:7,59:17,64:36,69:33,73:1,83:19,92:51,95:24,98:28}
     if points in snakes.keys():
          print('SNAKE')
          return snakes[points]
     else:
          return points
def reached_end(points):
     if points==end:
          return True
     else:
          return False
     
def play():
     p1_name = input('Enter player 1 name : ')
     p2_name = input('Enter player 2 name : ')
     pp1=0
     pp2=0
     turn=0
     while(1):
          if turn%2==0:
               print(p1_name, 'Your turn')
               c=input('Press 1 to continue, 0 to quit : ')
               if c==0:
                    print(p1_name,' SCORED : ',pp1)
                    print(p2_name,' SCORED : ',pp2)
                    print('Quitting the game, Thanks for playing ')
                    break
               dice=random.randint(1,6)
               print('DICE SHOWED :: ',dice)
               if not pp1+dice > end:
                    pp1+=dice
               pp1=check_ladder(pp1)
               pp1=check_ladder(pp1)
                    
               print(p1_name,' YOUR SCORE : ',pp1)
               if reached_end(pp1):
                    print(p1_name, 'WON')
                    break
          else:
               print(p2_name, 'Your turn')
               c=input('Press 1 to continue, 0 to quit : ')
               if c==0:
                   print(p1_name,' SCORED : ',pp1)
                   print(p2_name,' SCORED : ',pp2)
                   print('Quitting the game, Thanks for playing ')
                   break
               dice=random.randint(1,6)
               print('DICE SHOWED :: ',dice)
               if not pp2+dice > end:
                    pp2+=dice
               pp2=check_ladder(pp2)
               pp2=check_ladder(pp2)
               
               print(p2_name,' YOUR SCORE : ',pp2)
               if reached_end(pp2):
                    print(p2_name, 'WON')
                    break
          turn=turn+1
            
show_board()
play()