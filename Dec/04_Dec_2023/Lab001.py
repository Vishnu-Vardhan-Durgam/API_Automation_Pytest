import requests


# API
# requests Lib
# make a GET, POST , PUT. PATCH and DELETE and Verify

def main():
    response_body = requests.get(
        "https://restful-booker.herokuapp.com/booking/6")  # If booking ID exists we will get RC = 200
    print(response_body.text)  # response in DOUBLE COTS ("")
    print(response_body.status_code)
    print(response_body.json())  # response in SINGLE COTS ('')
    if response_body.status_code == 200:
        print("TC#1 -Get request is successful")  # If booking ID exists we will get this message
    else:
        print("TC#1 -Get request is not successful")  # If booking ID exists we will get this message


# to make an API Testing req.
#  URL , auth , headers , cookies , data(payload) , JSON file

# Validate in API testing
# response , headers , status code , response time , JSON schema validation


if __name__ == "__main__":
    main()
