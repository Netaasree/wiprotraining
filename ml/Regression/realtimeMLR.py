import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#age,milage,owners,engine cubic size
x=np.array([
    [3,40,1,2.0],
    [5,70,2,1.6],
    [1,30,1,2.5],
    [8,90,3,1.8],
    [6,80,2,2.0],
    [2,50,1,2.2],
    [4,60,1,1.5],
    [7,85,3,1.6]
])
y=np.array([20,15,25,10,12,22,18,11])

model=LinearRegression()
model.fit(x,y)
print("Intercept:",model.intercept_)
print("Coefficents:",model.coef_)
newcar=np.array([[4,55,2,1.8]])

predicted_price=model.predict(newcar)
print(f"Predicted price for the car: ${predicted_price[0]*1000:.2f}")

y_pred=model.predict(x)
plt.scatter(y,y_pred,color='blue')
plt.plot([y.min(),y.max()],[y.min(),y.max()],'r--',lw=2)
plt.xlabel("Actual prize in $1000")
plt.ylabel("Predicted prize in $1000")
plt.title("Original vs Predicted")
plt.show()