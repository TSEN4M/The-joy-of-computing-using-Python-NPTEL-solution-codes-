import random
#open the file in read mode with r and write mode with w and as both r+ also 'a' mode for appned at end of line
with open("file1.txt","r+") as myfile: 
    print(myfile.read())
    myfile.write("I am fine", end="\n")
myfile.close()
