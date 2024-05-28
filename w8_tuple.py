#tuple imutable   tuples can not be updated or made changes but can be deleted as whole

ice_cream_flavour=('vanila','chocolate','butterscotch','strawberry')
print(ice_cream_flavour)

for flavour in ice_cream_flavour:
     print(flavour)
     
del ice_cream_flavour
#print(ice_cream_flavour) #throws error not defined

toy=(1,2,3,4,5,6,7,3,4,2,6,7,2,9)
print(toy.count(2))
print(toy.index(9))

#tuples are used in image processing