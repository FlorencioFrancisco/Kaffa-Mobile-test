from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

URL = 'http://worldtimeapi.org/api/timezone'

@app.route('/currentDateTime/<string:location>/<string:area>', methods=['GET']) # returns the current date time of the especified location/area
def GetDateTime(location, area):                                                # locations and areas can be checked in the /locationsAvailable url
    response = requests.get(URL+'/'+location+'/'+area)
    if(response.status_code!=200):
        return response.status_code
    return jsonify({"currentDateTime": response.json()['datetime']}), 200

@app.route('/locationsAvailable',methods=['GET']) # returns the list of available location for date time requests
def GetLocations():
    response = requests.get(URL)
    if(response.status_code!=200):
        return response.status_code
    return jsonify({'locations': response.json()}), 200

if __name__ == '__main__': # the local server will be running in localhost:5000
    app.run(debug=True)