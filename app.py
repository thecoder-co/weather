from flask import *
from flask_restful import *
import json, requests, sys


Location='London,uk'

APP_ID='9921065396d054a0f07bcfeb4bc50cd1'

app = Flask(__name__)
api = Api(app)

#CORS(app, resources={r"*": {"origins": "*"}})

url='http://api.openweathermap.org/data/2.5/weather?q='+Location+'&APPID='+APP_ID


class Profile(Resource):
    #@cross_origin()
    def get(self):
        response= requests.get(url)
        response.raise_for_status()
        # get the identity from the jwt
        weatherData = json.loads(response.text)
        w=weatherData['weather']
        print('Current weather in %s:' % (weatherData["name"]))
        print(w[0]['description'])
        print('The maximum temperature in Kelvin is %s:' % (weatherData["main"]["temp"]))

        return {'status_code': 200, 'body': response.text, 
        'current_weather': f'Current weather in {weatherData["name"]}: is {w[0]["description"]}',
        'max_temp': 'The maximum temperature in Kelvin is %s:' % (weatherData["main"]["temp"]),

        }, 200



api.add_resource(Profile, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
