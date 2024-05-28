L = [int(i) for i in input().split()]
#for a in range(len(L)):
#    if(a%2!=0):
#        if(len(L)-a<=2):
#            print(L(a))

L.sort()
print(L[:3])
L.reverse()
print(L[:2])   
        