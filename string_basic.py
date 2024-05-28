import string

S="Ngawang"

print(S.lower())
print(S.upper())
Sl=list(S)
print(Sl)
print(S.replace("a","#"))          #replace a string a with # substring can also be given
Sl=list(S)
print(Sl)
                         #slicing of list
print(Sl[1:4])
print(Sl.index('g'))          #first occurance of the string in the Sl