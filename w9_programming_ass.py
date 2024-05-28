#programming assignment 

def subStr(s1, s2):
    M = len(s1)
    N = len(s2)
 

    for i in range(M - N + 1):
        flag = True
        for j in range(N):
            if (s1[i + j] != s2[j]):
                flag = False
                break
             
        if flag :
            return True
 
    return False
if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(subStr(s1, s2))

#programming assignment 2
n = int(input('Enter a number : '))
n = str(n)
d = {}
for i in range(len(n)):
    if n[i] not in d.keys():
        d[n[i]] =  [i]
    else:
        d[n[i]].append(i)
        
        
for key, value in d.items():
    print(key, end= ' ')
    for i in value:
        print(i, end= ' ')
        
    print()
