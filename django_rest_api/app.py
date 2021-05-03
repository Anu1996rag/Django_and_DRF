import requests
import json

URL = "http://127.0.0.1:8000/student_api"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {
            "id": id
        }
    json_data = json.dumps(data)
    response = requests.get(URL, data=json_data)
    print(response.json())


def update_data():
    body = {
        "id": 2,
        "name": "anu"
    }
    json_data = json.dumps(body)
    response = requests.put(URL, data=json_data)
    print(response.json())


def delete_data():
    body = {
        "id": 2
    }
    json_data = json.dumps(body)
    response = requests.delete(URL, data=json_data)
    print(response.json())


def create_data():
    data = {
        "name": "asdf",
        "roll": 100,
        "city": "bgm"
    }
    json_data = json.dumps(data)
    response = requests.post(URL, data=json_data)
    print(response.json())


create_data()
