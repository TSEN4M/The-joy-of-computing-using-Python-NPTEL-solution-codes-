#q1
import string
def shift(word,value):
     letters=string.ascii_lowercase
     new=''
     for i in range(len(word)):
          if word[i] in letters:
               index=letters.index(word[i])
               new=new+letters[(index+value%26)]
               print(new)
          else:
               new=new+word[i]
     return new

new_word=shift('dog',2)
print(new_word)               #shift every letters in a given word by 'value'

def recursive(L):
     if(len(L)<=6):
          print(L[-1])
          print(L[:-1])
          return L[-1]
     return L[-1] * recursive(L[:-1])
print(recursive([1,2,3,4,5,6,7,8,9,10]))          #print the product of elements in array from 5th index

#using index function
P=[2,41,45,12,51,53,522,521,25,56,234,17,165,436,235]
a=int(input('enter the planet to find'))
print(sorted(P).index(a-1)+1)

#w6 assingnment 2
import string
S=input('Enter a string : ')
ans=""
lower=string.ascii_lowercase
upper=string.ascii_uppercase
for i in (S):
     if i in lower:
          index=lower.index(i)
          index=((index-2)+26)%26
          ans+=lower[index]
     elif i in upper:
          index=upper.index(i)
          index=((index-3)+26)%26
          ans+=upper[index]
     else:
          ans+=i
print(ans)