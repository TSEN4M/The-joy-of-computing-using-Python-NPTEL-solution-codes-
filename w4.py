row = int(input("enter the number of rows "))
for i in range(1,row+1):
   for j in range(1,row+1):
      if j<=row-i:
         print(" ",end="")
      else:
         print("*",end="")
   print()

s=input("Enter a String")

