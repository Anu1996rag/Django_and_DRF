import requests
import json

URL = "http://127.0.0.1:8000/student_api/"
headers = {'content-type': 'application/json'}


def get_data():
    response = requests.get(URL, headers=headers)
    print(response.json())


def partial_update_data():
    body = {
        "id": 4,
        "name": "anu"
    }
    json_data = json.dumps(body)
    response = requests.patch(URL, data=json_data, headers=headers)
    print(response.json())


def delete_data():
    body = {
        "id": 2
    }
    json_data = json.dumps(body)
    response = requests.delete(URL, headers=headers, data=json_data)
    print(response.json())


def create_data():
    data = {
        "name": "asdf",
        "roll": 100,
        "city": "bgm"
    }

    json_data = json.dumps(data)
    response = requests.post(URL, data=json_data, headers=headers)
    print(response.json())


partial_update_data()
