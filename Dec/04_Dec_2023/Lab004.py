import requests


def main():
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
    assert data["firstname"] == "Mary", "Incorrect firstName"
    assert data["lastname"] == "Ericsson", "Incorrect lastName"
    assert data["bookingdates"]["checkin"] == "2018-03-03", "incorrect message"
    #  We can verify other values as well like TOTAL PRICE , DEPOSIT PAID , CHECKIN & CHECKOUT

if __name__ == '__main__':
    main()
