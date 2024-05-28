import string
#binary sort
def binary_sort(numbers):  
     for i in range(len(numbers)):
          for j in range(len(numbers)-i-1):
               if numbers[j]>numbers[j+1]:
                    temp=numbers[j]
                    numbers[j]=numbers[j+1]
                    numbers[j+1]=temp
     print('after sorting ',numbers)

def binary_search(element,x):
     flag=0
     count=0
     first_pos=0
     last_pos=len(element)-1
     while first_pos<=last_pos and  flag==0:
          mid=(first_pos+last_pos)//2
          if x==element[mid]:
               flag=1
               print('the numbers is found at pos : ', str(mid))
               return
          elif x>element[mid]:
               first_pos=mid+1
          elif x<element[mid]:
               last_pos=mid-1  
         
numbers=[0]*5
print('enter five numbers ')
for i in range(5):                                                                                                                                                                                                                                                                                                                             
     numbers[i]=int(input())
print('the numbers before sorting ',numbers)
binary_sort(numbers)


#binary search
element=[]
for i in range(1001):
     element.append(i)
print(element)
binary_search(element,100)
