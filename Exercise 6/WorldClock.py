import requests

# in this exersice the server url was returning 403 so I decided to use an alternative api

URL = 'http://worldclockapi.com/api/json/utc/now' # defining endpoints
URL2 = 'http://worldtimeapi.org/api/timezone'     # alternative api
LOCATION = '/America/Sao_Paulo'                   # my current location

def GetDate(url):
    request = requests.get(url) # make the requets

    if (request.status_code == 200):
        response = request.json()  # get response in json
        #print(response)
        return response['datetime']  # get desired data
    else:
        return 'error ' + str(request.status_code)

print(GetDate(URL))

print(GetDate(URL2+LOCATION))