#q1
t=(1,2,3,4,5)
for i in range(-1,-len(t),-1):
     print(t[i],end=',')
     
#q2
word='facebook'
new=''
for w in word:
     i=ord(w)
     print('unicode point is : ',i)
     j=(((i+26)-97)%26)+97
     new =new+chr(j)
     print('new is : ',new)
print(new)

#programming assignment 1
'''
def squareT(T):
     for i in range(len(T)):
          print(T[i],end=' ')
     for i in range(len(T)):
          print((T[i])*T[i],end= ' ')

T=(1,2,3)
squareT(T)
'''
def squareT(T):
    temp = list(T)
    for i in T:
        temp.append(i*i)
    return tuple(temp)
if __name__ == "__main__":
    #n = int(input())
    L = list(map(int, input().split()))
    T = tuple(L)
    ans = squareT(T)
    if type(ans) == type(T):
        print(ans)

#programming assignment 2 replaceing 3 consecutive vovels with '_'
def isvowel(ch):
    v = 'AEIOUaeiou'
    if ch in v:
        return True
    
    else:
        return False

def replaceV(s):
    
    n = len(s)
    ans = ''
    i=0
    while(i<n-2):
        if isvowel(s[i]) and isvowel(s[i+1]) and isvowel(s[i+2]):
            ans = ans+'_'
            i = i+3
            
        else:
            ans = ans+s[i]	

            i = i+1
            
    return ans+s[i:]
S = input()
print(replaceV(S))

#programming assignment 3 shifting all zeros to right

sol=[]
def shift(N):
     for i in range(len(N)):
          if N[i]==0:
               print('equal to 0')
               sol.insert((len(N)-i-1),N[i])
          else:
               print('not equal to 0')
               sol.insert(i,N[i])
          print(sol)
print(sol)
N=[0,1,0,2,3,4,0,5]
shift(N)