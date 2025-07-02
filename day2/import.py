import json
name=input("Enter the name:")
age=int(input("Enter age:"))

user={"name":name,"age":age}

with open("user.json",'w') as f:
    json.dump(user,f)
print("Data written to json folder")

with open("user.json",'r') as f:
    loaded=json.load(f)
    print("Read from file",loaded)

with open("newfile.json", 'w') as f:
    json.dump(user,f)

with open("newfile.json", 'r') as f:
    loaded1 = json.load(f)
    print("new file is loaded")

demonslayer = ['tanjiro', 'zenitsu','kingdom','zoro','inosuke','ninja','hattori','naruto','Ben10']
with open("cartoon.json",'w') as f:
    json.dump(demonslayer,f)
    print("write complete")
with open("cartoon.json",'r') as f:
    s=json.load(f)
    print("data is: ",s)