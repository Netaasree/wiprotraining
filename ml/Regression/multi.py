import pickle

my_list=[10,2,3,'vijay',True]
with open('Regression/list.pkl','wb') as f:
    pickle.dump(my_list,f)
with open('Regression/list.pkl','rb') as f:
    loaded_list=pickle.load(f)
print(loaded_list)