import datetime
import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_number = ""
api_key = ""
aqi_end_point = "http://api.openweathermap.org/data/2.5/air_pollution"

my_home_location = {
    "longitude": 74.405818,
    "latitude": 16.616344,
}

parameters = {
    "lat": my_home_location['latitude'],
    "lon": my_home_location['longitude'],
    "appid": api_key,
}

aqi_response = requests.get(url=aqi_end_point, params=parameters)
aqi_response.raise_for_status()
AQI = ""
if int(aqi_response.json()['list'][0]['main']['aqi']) == 1:
    AQI = f"\nTime Stamp:{datetime.datetime.now()}\nGood Air Quality "
elif int(aqi_response.json()['list'][0]['main']['aqi']) == 2:
    AQI = f"\nTime Stamp:{datetime.datetime.now()}\nFair Air Quality"
elif int(aqi_response.json()['list'][0]['main']['aqi']) == 3:
    AQI = f"\nTime Stamp:{datetime.datetime.now()}\nModerate Air Quality"
elif int(aqi_response.json()['list'][0]['main']['aqi']) == 4:
    AQI = f"\nTime Stamp:{datetime.datetime.now()}\nPoor Air Quality"
elif int(aqi_response.json()['list'][0]['main']['aqi']) == 5:
    AQI = f"\nTime Stamp:{datetime.datetime.now()}\nVery Poor Air Quality"

AQI_components = "AQI Components (microgram/volume):"

for component in aqi_response.json()['list'][0]["components"]:
    AQI_components += f"\n{component}: {aqi_response.json()['list'][0]['components'][component]}"

weather_reponse = requests.get(url= f"https://api.openweathermap.org/data/2.5/weather?q=hupari,in&appid={api_key}&units=metric")
weather_reponse.raise_for_status()
weather = weather_reponse.json()['weather'][0]['main']

temperature = ""
temp = weather_reponse.json()['main']
for t in temp:
    temperature += f"\n{t}: {temp[t]}"

visibility = int(weather_reponse.json()['visibility'])/1000

wind_specification = "Wind Specification: "
wind = weather_reponse.json()['wind']
for w in wind:
    wind_specification += f"\n{w}: {wind[w]}"


client = Client(account_sid, auth_token)

message = client.messages.create(
                              messaging_service_sid='',
                              body=f"{AQI}\n{AQI_components},\ntoday weather: {weather},\n{temperature},\nvisibility: {visibility}km,\n{wind_specification}.",
                              to=''
                          )

print(message.status)