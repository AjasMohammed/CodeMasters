import requests
from api_key import API_KEY


def check_wether(url):
    response = requests.get(url)
    data = response.json()

    pharse_data(data)

def pharse_data(data):
    wether_location = data['location']
    place = wether_location['name']
    region = wether_location['region']
    country = wether_location['country']

    conditions = data['current']

    temp_c = conditions['temp_c']
    temp_f = conditions['temp_f']
    humidity = conditions['humidity']


    print(f"""
    Location: {place}
    Region: {region}
    Country: {country}
            ---------------------------------
            Temperature in Celcius: {temp_c}C
            Temperature in Fahrenheit: {temp_f}F
            Humidity: {humidity}
            ---------------------------------
            \n
    """)

while True:
    location = input('Enter Location: ')
    api_url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"

    try:
        check_wether(api_url)
    except:
        print('Enter a valid location')