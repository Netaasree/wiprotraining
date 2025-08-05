import pandas as pd
try:
    df=pd.read_csv('pandas/hospital.csv')
    print("\n Original Hospital DataFrame")
    print(df)
#user manual input
    print("\n Enter Patient_ID to update")
    patient_id=input().strip()
    print("Enter new Bill for {patient_id}:")
    new_cost=float(input())
#update bill series and save
    if patient_id in df['Patient_ID'].values:
        index=df[df['Patient_ID']==patient_id].index[0]
        series[index]=new_cost
        print("\n Updated medical bill series.")
        print(series)
#update DataFrame and save
        df['Bill']=series
        df.to_csv('hospital_data.csv',index=False)
        print("Updated csv saved to 'hospital_data.csv' ")
    else:
        print(f"Error:patient_id {patient_id} not found.")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found")
        