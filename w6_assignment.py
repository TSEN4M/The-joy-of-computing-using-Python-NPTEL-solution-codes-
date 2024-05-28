import string
sma=string.ascii_lowercase
cap=string.ascii_uppercase
ans=''

S=input()
for i in S:
     if i in sma:
          index=sma.index(i)
          index=((index-2)+26)%26
          if sma[index]=='c':
               ans+='c'
          ans+=sma[index]
     elif i in cap:
          index=cap.index(i)
          index=((index-3)+26)%26
          if cap[index]=='D':
               ans+='A'
          ans+=cap[index]
     else:
          ans+=i
print(ans)