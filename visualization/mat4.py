import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.figure(figsize = (10,6),dpi = 100)
plt.plot(x,y, color ='Red',ls=':',lw=4,marker='o',markerfacecolor='green',
         markersize=8,markeredgecolor='black')
plt.title("Line Plot Referal", fontsize = 16, fontweight = 'bold', color = 'blue')
plt.xlabel("Years of working", fontsize = 12)
plt.ylabel("Profit in Millions", fontsize = 12)
plt.gca().set_facecolor('yellow')
plt.gcf().set_facecolor('brown')

plt.grid(True,linestyle='--',lw=3,alpha=0.7)
plt.show()