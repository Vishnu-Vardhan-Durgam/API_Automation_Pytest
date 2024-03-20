import requests
import pytest


def create_token():
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
    return token

def create_booking():
    print("Create a booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)


    # assertions
    assert response.status_code == 200
    # get the response body and verify the JSON ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_requests():
    # booking ID and Token
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL+str(booking_id)
    cookie_value = "token=" +create_token()
    headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
                 }
    print(headers)
    json_payload = {
        "firstname": "vvv",
        "lastname": "vardhan",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)

    # assertions
    assert response.status_code == 200
    # get the response body and verify the JSON ID is not None
    data = response.json()
    print(data)
    assert data["firstname"] == "vvv", "incorrect firstName"


def test_delete():

    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
            }
    print(headers)
    response = requests.delete(url=PUT_URL, headers=headers)

    # assertions
    assert response.status_code == 201

# try:
# except Exception as e:
# print(e)







