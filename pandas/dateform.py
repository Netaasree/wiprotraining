import pandas as pd
try:
    df=pd.read_csv('hospital_data.csv')
    series=df['Admission_Date']
    print("\n Original Admission_Date series")
#convert string to datetime
    date_series=pd.to_datetime(series,format='%Y-%m-%d')
    print("\n Admission Date series after converting to datetime:")
    print(date_series)
#update and save the dataframe
    df['Admission_Date']=date_series
    df.to_csv('hospital_data.csv',index=False)
    print("\n updated csv saved to 'hospital_data.csv'")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found.")