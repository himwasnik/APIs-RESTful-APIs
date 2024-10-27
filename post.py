import requests

data ={
    "name": "morpheus",
    "job": "leader"
}

response = requests.post("https://reqres.in/api/users", json=data)
print(response.status_code)
print(response.json())