import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
hours=np.array([1,2,3,4,5]).reshape(-1,1)
marks=np.array([2,4,6,4,5])
model=LinearRegression()
model.fit(hours,marks)
#wild pointer-it can access data form any where

new_hours=np.array([[6]])
prediction=model.predict(new_hours)
print(f"predicted marks for 6 hours:{prediction[0]:.2f}")

plt.scatter(hours,marks,color='blue',label="Original data")
plt.plot(hours,model.predict(hours),color='red',label='Regression line')
plt.xlabel("Hours studied")
plt.ylabel("Scored marks")
plt.legend()
plt.show()