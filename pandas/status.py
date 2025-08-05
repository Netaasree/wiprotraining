import pandas as pd
try:
    df=pd.read_csv('pandas/hospital_data.csv')
    print("\n original Hospital DataFrame")
    print(df)
#Add a status column,based on age
    df['Status']=df['Age'].apply(lambda x:'senior' if x>=50 else
                                 'Adult' if x>=18 else 'unkown')
    print("\n Data frame with status column")
    print(df)
#saving to csv
    df.to_csv('pandas/hospital_data_updated.csv',index=True)
    print("\n Modified Dataframe saved to 'hospital_data_updated.csv")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found")