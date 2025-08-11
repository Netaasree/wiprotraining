import pickle
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hi(self):
        return f"Hello , my name is {self.name}"

s=Student('Netaasree',34)
with open('student.pkl','wb') as f:
    pickle.dump(s,f)
with open('student.pkl','rb') as f:
    loadeddata=pickle.load(f)

print(loadeddata.name)
print(loadeddata.hi())