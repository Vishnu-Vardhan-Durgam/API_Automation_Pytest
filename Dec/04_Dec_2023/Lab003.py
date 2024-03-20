
import requests


def main():
    # id  = 6
    # url = "https://restful-booker.herokuapp.com/booking/"
    # full_url = url + str(id)
    # response_body = requests.get(full_url)
    
    #  OR

    response_body = requests.get("https://restful-booker.herokuapp.com/booking/6")
    assert response_body.status_code == 200

# If ID does not exist will get " AssertionError "

if __name__ == '__main__':
    main()
