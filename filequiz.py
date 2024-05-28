
def sum_of_list(S):
    total=0
    
    for i in range(len(S)):
        total=total+S[i]
        
    return total
S=[1,2,3,4,5,6,7,8,9,10]

total_sum=sum_of_list(S)
print(total_sum)

with open('file.txt', 'w') as file:
    file.write('hey there!')
file.close()

with open('file.txt','a') as file:
    file.write('writing this file again')
    
with open('file.txt','r') as file:
    print(file.read())

#with open('file.txt','r') as file:
#    print(file.read())
#    file.write('hey there !!')
#file.close()

with open('file.txt','w') as file:
    file.write('1000111011')
file.close()

with open('file.txt','r') as file:
    P=list(file.read())
file.close()

for i in range(len(P)):
    if(i%2==0 and P[i]=='0'):
        P[i]='1'
    if(i%2 !=0 and P[i]=='1'):
        P[i]='0'
print(P)