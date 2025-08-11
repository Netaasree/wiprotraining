import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(42)
x=np.random.rand(100)*10
#n=3x+5
y=3*x+5+np.random.randn(100)*2

m,c = np.polyfit(x,y,1)
print(f"slope(m):{m:.2f}")
print(f"Intercept(c):{c:.2f}")

newx=9
print(f"Predicted y for x={newx}:{m*newx+c:.2f}")

plt.scatter(x,y,color='blue',alpha=0.6,label='DataPoints')
plt.plot(x,m*x+c,color='red',lw=2,label='Best fitted line')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.legend()
plt.show()