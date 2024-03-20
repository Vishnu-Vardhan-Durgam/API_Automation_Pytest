import pytest
import requests


def test_sample1():
    assert 4 == 4


def test_sample2():
    assert 6 == 5


def test_get_request():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/7")
    assert response_body.status_code == 200

    # assertions
    data = response_body.json()
    # print(data)

    # Verifying keys
    assert 'firstname' in data, "firstName key is Present"
    assert 'lastname' in data, "lastName key is Present"
    #  We can verify other keys as well like TOTAL PRICE , DEPOSIT PAID , CHECKIN & CHECKOUT

    # Verifying Values
    assert data["firstname"] == "Eric", "Incorrect firstName"
    assert data["lastname"] == "Jones", "Incorrect lastName"
    assert data["bookingdates"]["checkin"] == "2022-03-09", "incorrect message"
    #  We can verify other values as well like TOTAL PRICE , DEPOSIT PAID , CHECKIN & CHECKOUT
