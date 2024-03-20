# create booking
#  URL , HEADER , Body (payload) , No auth needed
# Verify the booking INFO as JSON
import requests
import pytest

@pytest.mark.positive
def test_create_booking_positive():...

@pytest.mark.negative
def test_create_booking_negative():...

@pytest.mark.positive
def test_create_booking_positive():
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
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "incorrect firstName"



def test_create_booking_negative():
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
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Amit", "incorrect firstName"
