from flask import *
from flask_restful import *
import requests


locations_list=['London,uk', "Lagos,ng"]

APP_ID='9921065396d054a0f07bcfeb4bc50cd1'

app = Flask(__name__)
api = Api(app)

#CORS(app, resources={r"*": {"origins": "*"}})

url='http://api.openweathermap.org/data/2.5/weather?q='

def get_res(location):
    return requests.get(url + location+'&APPID='+APP_ID)

class GetWeather(Resource):
    #@cross_origin()
    def get(self):
        locations_data = []
        for location in locations_list:
            response = get_res(location)
            response.raise_for_status()
            locations_data.append(response.json())

        weatherData = json.loads(json.dumps(locations_data))
        # w=weatherData['weather']
        # print('Current weather in %s:' % (weatherData["name"]))
        # print(w[0]['description'])
        # print('The maximum temperature in Kelvin is %s:' % (weatherData["main"]["temp"]))
        data = {'status_code': 200, 'body': weatherData,}
        for i in locations_data:
            w=i['weather']
            name = i['name']
            description = w[0]['description']
            temp = i['main']['temp']
            data[f'current_weather_{name}'] = f'Current weather in {name}: is {description}'
            data[f'max_temp_{name}'] = f'The maximum temperature in Kelvin is {temp}'

        return data, 200



api.add_resource(GetWeather, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
