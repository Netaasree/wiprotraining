import pandas as pd
import matplotlib.pyplot as plt

try:
    df=pd.read_csv('hospital_data.csv')
    cost_series=df['Bill']
    date_series=df['Admission_date']
    print("\n original Bill series:")
    print(cost_series)
    print("\n original Date series:")
    print(date_series)
#user input for cleaning and plotting
    print("\n Fill the missing Bill value with median before plotting?(yes/no): ")
    fill_confirm=input().strip().lower()
    print("Convert ADMISSION DATE TO DD/MM/YYYY for display?(yes/no): ")
    date_format_confirm=input().strip().lower()
#perfom clean bill missing values
    if fill_confirm=='yes':
        median_cost=cost_series.median()
        cleaned_cost_series=cost_series.fillna(median_cost)
        print(cleaned_cost_series)
    else:
        print("\n No changes to medical cost.")
#convert admission date to datetime
    cleaned_date_series=pd.to_datetime(date_series,format='%Y-%m-%d',errors='coerce')
    if date_format_confirm=='yes':
        display_dates=cleaned_date_series.dt.strftime('%d-%m-%Y')
    else:
        display_dates=cleaned_date_series
#plot
    plt.figure(figsize=(10,6))
    plt.plot(cleaned_date_series,cleaned_cost_series,marker='o',ls='-',color='blue')
    plt.title("medical cost over Admission dates")
    plt.xlabel("Admission Date")
    plt.ylabel("medical cost($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
#update and save 
    if fill_confirm=='yes' or date_format_confirm=='yes':
        df['Bill']=cleaned_cost_series
        df['Admission_date']=display_dates if date_format_confirm=='yes' else cleaned_date_series
        df.to_csv('hospital_data.csv',index=False)
        print("\n Updated csv saved to 'hospital_data.csv'")
    else:
        print("\n Not updated")
except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found.")
except ValueError as e:
    print("Error: Invalid date format({e}).")
        
        
        
    
    