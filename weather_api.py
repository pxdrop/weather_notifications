import requests
from id_converter import idconverter

api_key = ""
def tempconvert(k):
    celsius = int(k) - 273.15
    return format(celsius, ".2f")

def mmconverttoinches(mm):
    inches = int(mm)/25.4
    return format(inches, ".2f")

def winddirection(deg):
    deg = int(deg)
    if deg in range(22, 67):
        direction = "NE"
    elif deg in range(68, 112):
        direction = "E"
    elif deg in range(113, 157):
        direction = "SE"
    elif deg in range(158, 202):
        direction = "S"
    elif deg in range(203, 247):
        direction = "SW"
    elif deg in range(248, 292):
        direction = "W"
    elif deg in range(293, 337):
        direction = "NW"
    elif deg in range(338, 360):
        direction = "N"
    elif deg in range(0, 21):
        direction = "N"
    return direction


def by_zipcode():
    zipcode = 77093
    url = (f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={api_key}")
    print(url)
    res = requests.get(url).json()
    print(res)

    temp_kelvin = res['main']['temp']
    mintemp_kelvin = res['main']['temp_min']
    maxtemp_kelvin = res['main']['temp_max']
    wind_deg = res['wind']["deg"]
    weather_id = res['weather'][0]['id']
    weather_num = int(weather_id)


    temp = tempconvert(temp_kelvin)
    mintemp = tempconvert(mintemp_kelvin)
    maxtemp = tempconvert(maxtemp_kelvin)
    humidity = res['main']['humidity']
    wind_speed = res['wind']['speed']
    wind_direction = winddirection(wind_deg)
    weather_code = idconverter(weather_num)
    print(weather_code)

#    print(f'Temperature: {temp}C \nMinimum Temperature: {mintemp}C \nMaximum Temperature: {maxtemp}C \n'
#          f'Humidity: {humidity}% \nWind Speed: {wind_speed} Mph \nWind Direction: {wind_direction}')
    return temp, mintemp, maxtemp, humidity, wind_speed, wind_direction, weather_code
