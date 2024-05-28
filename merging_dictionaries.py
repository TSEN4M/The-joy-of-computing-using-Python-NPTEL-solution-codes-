d1={1:1,2:2,3:3}
d2={4:4,3:3,6:6}

def merg_dic(d1,d2):
     d3={}
     for key,value in d1.items():
          d3[key]=value
     
     for key,value in d2.items():
          if key not in d3.keys():
               d3[key]=value
     return d3

print(merg_dic(d1,d2))