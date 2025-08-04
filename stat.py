'''
code to show the computation of statstics and access series ttriute 
100,200,150,300,250
print original data,which is serialized 
statastics:
mean sum max min
attributes:
index=['a'......'e']
values=[100.0.......250.0]
'''

import pandas as pd
print("Enter 5 random numbers,space seperated: ")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=5:
        raise ValueError("Please enter 5 numbers only!!!")
    series=pd.Series(numbers,index=['a','b','c','d','e'])
    print("\n original series: ")
#statistics
    print("\n Statics: ")
    print(f"Mean:{series.mean()}")
    print(f"sum:{series.sum()}")
    print(f"max:{series.max()}")
    print(f"min:{series.min()}")
#Attributes
    print("\n Attributes")
    print(f"Index:{series.index.tolist()}")
    print(f"values:{series.values.tolist()}")
    print(f"Datatype:{series.dtype}")

except ValueError as e:
    print(f"Error:{e}")