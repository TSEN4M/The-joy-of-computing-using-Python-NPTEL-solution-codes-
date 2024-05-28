ages = [12,1,3,44,32,54,64,74,33,67,78,93,34,67,22,56,3,2,55,33]
print(ages.count(3))
ages.sort()                     #sort in accending order by default
print(ages)
ages.reverse()                  #reverse the array order 
print(ages)

students=["Tsewang","Wangmo","Namgail","Dhargye","Kalden",]
print(students)
students.insert(0,"Friends")
print(students)
students.sort()
print(students)

#slicing    taking a part from the list 
#syntax   - list_name[start:end+1]
print(students[4:])        #by default start=0 and end = len(list)6 here
