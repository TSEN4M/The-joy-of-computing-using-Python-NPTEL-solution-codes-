#encrypting for secrecy
#substitute cipher
import string
dict={}
data=""
file=open("decoded.txt","w")
for i in range(len(string.ascii_letters)):
     dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("secret_message.txt") as f:
     while True:
          c=f.read(1)     #read the file argument place 1 
          if not c:      #reaached end of line
               print("End of File")
               break
          if c in dict:
               data=dict[c]
          else:
               data=c
          file.write(data)
          print(data)
file.close()