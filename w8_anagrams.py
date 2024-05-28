'''
x=[1,6,7,3,4]
print(sorted(x))
print(sorted(x,reverse=True))
x.sort()
print(x)
L=['a','cccc','ddd','bb']
print(sorted(L))
L.sort(key=len)
print(L)
print(sorted(L,key=len)) '''

str1=input('Enter the first string : ')
str2=input('Enter the second string : ')
print(sorted(str1))
print(sorted(str2))

if sorted(str1)==sorted(str2):
     print('These are anagrams ')
else:
     print('These are not anagrams ')