import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Hi students",
    "body":"wipro Geeks",
    "userId":1
}
response=requests.post(url,json=data)
print("status code",response.status_code)
print("Response json",response.json())