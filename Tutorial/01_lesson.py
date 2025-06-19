import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json() #converts the json response to dictionary
print(data)