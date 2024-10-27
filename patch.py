import requests

data = {
    "name": "morpheus"
}


response = requests.patch("https://reqres.in/api/users/2", json=data)

print(response.status_code) 
print(response.json())       
