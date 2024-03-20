import requests
import pytest


def test_create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=URL, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)






