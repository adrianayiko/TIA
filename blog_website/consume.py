# consuming an api as a client in blog_website
import requests

request = requests.get('http://127.0.0.1:8000/blog/apis/')
#print(request.json())

request1 = requests.get('http://127.0.0.1:8000/blog/apis/1')
print(request1.json())