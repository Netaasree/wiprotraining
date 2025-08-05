import pandas as pd
names=pd.Series(['aples','orangges','kiwi'])
df=names.to_frame(name='Name')
#add new column
df['Price']=[50,30,80]
print(df)