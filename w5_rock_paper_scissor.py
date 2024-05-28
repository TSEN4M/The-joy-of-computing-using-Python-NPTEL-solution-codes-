def rock_paper_scissor(num1,num2,bit1,bit2):                   
     #num1 is a string eg 12345 and we are selecting a secret bit and finding the value according to the dictionary
     p1=int(num1[bit1])%3 
     print(p1)
     p2=int(num2[bit2])%3
     print(p2)
     if player_one[p1]==player_two[p2]:
          print('Draw..')
     elif player_one[p1]=='rock' and player_two[p2]=='scissor':
          print('Player one Wins..')
     elif player_one[p1]=='rock' and player_two[p2]=='paper':
          print('Player two Wins..')
     elif player_one[p1]=='paper' and player_two[p2]=='scissor':
          print('Player two Wins..')
     elif player_one[p1]=='paper' and player_two[p2]=='rock':
          print('Player one Wins..')
     elif player_one[p1]=='scissor' and player_two[p2]=='rock':
          print('Player two Wins..')
     elif player_one[p1]=='scissor' and player_two[p2]=='paper':
          print('player one Wins..')

player_one={0:'rock',1:'paper',2:'scissor'}
player_two={0:'paper',1:'rock',2:'scissor'}
while(1):
     num1=input('Player one, Enter your choice ')
     num2=input('Player two, Enter your choice ')
     bit1=int(input('Player one, Enter the secret bit position '))
     bit2=int(input('Player two, Enter the secret bit position '))
     rock_paper_scissor(num1,num2,bit1,bit2)
     ch=input('Do you want to continue? y/n ')
     if ch=='n':
          break