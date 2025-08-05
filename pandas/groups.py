import pandas as pd
try:
    df=pd.read_csv('pandas/hospital_data.csv')
    print("\n original Hospital")
    print(df)
#Grouping by department
    grouped=df.groupby("Department")['Bill'].mean()
    print("\n Average Medical cost by Department")
    print(grouped)
except FileNotFoundError:
    print("Error: 'Hospital_data.csv' not found.")