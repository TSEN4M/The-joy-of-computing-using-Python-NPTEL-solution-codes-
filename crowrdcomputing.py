'''here we are estimating the number of marbles in a jar 
we are using matplotlib for ploting the graph '''

import statistics 
import matplotlib.pyplot as plt
#from scipy import stats
y=[]
Estimates=[100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234.250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720,1000,1010,1500,1500,1786,2000]
Estimates.sort()
print(Estimates)
print()
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
print(Estimates)
print()
Estimates=Estimates[:len(Estimates)-tv]
print(Estimates)
print()
print(statistics.mean(Estimates))
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([375],[5],"g^")
plt.plot([statistics.mean(Estimates)],5,'bs')
plt.plot([statistics.median(Estimates)],5,"b*")
plt.show()