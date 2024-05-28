conv_factor={}
conv_factor['dollar']=60
print(conv_factor)
conv_factor['euro']=80
print(conv_factor)
print(list(conv_factor))
print(conv_factor.keys())
print(conv_factor.values())
conv_factor['dollar']=65    #updating a value corresponding to key
print(conv_factor)
del conv_factor['euro']     #deleting a key here euro
print(conv_factor)
e=10
r=e*conv_factor['dollar']
print('The values in rupees for 10 dollar is : ', r)