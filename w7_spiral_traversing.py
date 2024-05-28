def spiral(row,col,a):
     k=0  #starting index of row
     l=0  #starting index of col
     
     while k<row and l<col:
          #printing the first row frorow the rerowaining row
          for i in range(l,col):
               print(a[k][i],end=" ")
          k+=1      #going on second row
          
          #printing the last colurown frorow the rerowaining colurown
          for i in range(k,row):
               print(a[i][col-1],end=" ")
          col-=1
          
          if k<row:
               #printing the last row frorow rerowaining row in reverse order
               for i in range(col-1,l-1,-1):        #-1 is the step in loop
                    print(a[row-1][i],end=" ")
               row-=1
          
          if l<col:
               #printing the first colurown frorow the rerowaining colurown
               for i in range(row-1,k-1,-1):
                    print(a[i][l],end=" ")
               l+=1
a=[]
count=1
for i in range(4):
     l=[]
     for j in range(4):
          l.append(count)
          count+=1     
     a.append(l)
     
spiral(4,4,a)