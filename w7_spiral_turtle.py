import turtle
from random import randint
turtle.bgcolor("black")
tur=turtle.Turtle()

width=5
height=7
dot_distance=20
tur.setpos(-250,250)          #always start from the centre

tur.penup()
list_color=['white','yellow','brown','red','blue','green','orange','pink','violet','grey','cyan']
def spiral(m,n): 
     
     k=0  #starting index of row
     l=0  #starting index of col
     flag=0
     col=randint(0,10)
     tur.color(list_color[col])
     
     
     while k<m and l<n:
          if flag==1:              #checking if the first row is printed
               tur.right(90)
          
             
          #printing the first row from the remaining row
          for i in range(l,n):
               tur.dot(3)
               tur.forward(dot_distance)
               #print(a[k][i],end=" ")
     
     
          k+=1      #going on second row
          flag=1
          
          
          tur.right(90)
          col=randint(0,10)
          tur.color(list_color[col])
          
          #printing the last column from the remaining column
          for i in range(k,m):
               tur.dot(3)
               tur.forward(dot_distance)
               #print(a[i][n-1],end=" ")
          n-=1
          tur.right(90)
          col=randint(0,10)
          tur.color(list_color[col])
          
          if k<m:
               #printing the last row from remaining row in reverse order
               for i in range(n-1,l-1,-1):        #-1 is the step in loop
                    tur.dot(3)
                    tur.forward(dot_distance)
                    #print(a[m-1][i],end=" ")
               m-=1
          tur.right(90)
          col=randint(0,10)
          tur.color(list_color[col])
          
          if l<n:
               #printing the first column from the remaining column
               for i in range(m-1,k-1,-1):
                    tur.dot(3)
                    tur.forward(dot_distance)
                    #print(a[i][l],end=" ")
               l+=1
               
spiral(20,20)
turtle.done()          