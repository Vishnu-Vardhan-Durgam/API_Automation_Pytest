import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/6")
print(response_body.text)
print(response_body.headers)


# Verify ??

#  Assertion --> Verify the expected result with the Actual result

#  response code/ If ID 6 exist  ---> ER == 200
#                                     AR == 200


#  response code/ If ID 6 not exist ---> ER == 404
#                                        AR == 404
