def factorial(n):
     if n==1:
          return 1
     else:
          return n * factorial(n-1)

print('factorial of 5 is : ',factorial(5))

def binary_search(arr,x,first,last):
     
     if first==last:
          if arr[first]==x:
               return first
          else:
               return -1
     else:
          mid=int((first+last)/2)
          if x==arr[mid]:
               return mid
          elif x<arr[mid]:
               return binary_search(arr,x,first,mid-1)
          else:
               return binary_search(arr,x,mid+1,last)

arr=[2,31,412,41,2,14,11,552,7]
arr.sort()
print(arr)

x=int(input('Enter a number to search :'))
index=binary_search(arr,x,0,len(arr)-1)
if index==-1:
     print(x,'not found')
else:
     print(x,'found at : ',index+1)