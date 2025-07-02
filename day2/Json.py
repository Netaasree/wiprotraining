#json module 
import json
sivaganesh = input("Enter your name: ")
age = int(input("Enter your age: "))
data = {"name" : sivaganesh, "age": age}
stringify_json = json.dumps(data)
print("Serialised data of JSON", stringify_json)
print(type(stringify_json))
