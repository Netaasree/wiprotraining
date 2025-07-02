import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts")
print("Status code:",response.status_code)
print("response JSON",response.json())

