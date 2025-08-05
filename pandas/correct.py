import pandas as pd
import numpy as np
try:
    df=pd.read_csv('hospital_data.csv')
    series=df['Age']
    print("\n Original age series: ")
    print(series)
#replace invalid ages,<0 or 120> with Nan
    clean_series=series.where((series>=0)&(series<=120),np.nan)
    print("\n Age series after replacing invalid ages with Nan:")
    print("clean_series")
    df['Age']=clean_series
    df.to_csv('hospital_data.csv',index=False)
    print("\n updated csv saved to 'hospital_data.csv'.")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found.")