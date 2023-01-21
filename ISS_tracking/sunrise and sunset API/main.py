import requests

# Hupari location
parameters = {
        "lat":16.620600,
        "lng":74.402397,
        "formatter" : 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data)

# getting sunset and sunrise from url
#response = requests.get('https://api.sunrise-sunset.org/json?lat=16.620600&lng=74.402397')


