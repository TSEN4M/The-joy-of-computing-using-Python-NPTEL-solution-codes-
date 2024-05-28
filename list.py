#list
shopping=["Bread","Coffee","Sugar"]     #array declaration
print(shopping)
print(end="\n")

for i in range(3):                      #i = 0 here
    print(i)
for item in shopping:                   #item is a identifier //can be replaced with anything
    print(item)
print(end="\n")

# to add another element to the list or array at the end
#append
shopping.append("Curd")
print(shopping)

for things in shopping:                 #things is a new identifier given to same variable 
    print(things)
print(end="\n")
#to put the items at a position in the list or array
print(shopping[1])
print(end="\n")                                     

for i in range(4):                      # #for(i=0; i<4;i++)
    print(shopping[i])
print(end="\n")

# insert at a position in list or array
# insert
shopping.insert(1,"Oil")
for item in shopping:
    print(item)

ages=[12,32,4,5,65,30,24,3,7,9,12,4,12]             # to count specific item -> count()  list_name.count(item)
print("the no 12 present ",ages.count(12))

# to the total number of items in the list or length of the list
print("the len of list ages is", len(ages))
