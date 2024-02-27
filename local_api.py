import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = 'http://127.0.0.1:8000'
api_response = requests.get(r)

# TODO: print the status code
print("Status Code: ", api_response.status_code)

# TODO: print the welcome message
print("json Response: ", api_response.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = "http://127.0.0.1:8000/data/"
post_message = requests.post(r, json = data)


# TODO: print the status code
print("Status Code: ", post_message.status_code)

      
# TODO: print the result
print("Response JSON: ", post_message.json())
