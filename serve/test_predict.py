import requests

endpoint = 'http://localhost:8080/predict'

input_data = {
    "petal_lenght": 4.5,
    "petal_width": 1.2,
}

response = requests.post(url=endpoint, json=input_data)

print(response)
print(response.json())
