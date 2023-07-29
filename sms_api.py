import vonage
api_key = ""
api_secret = ""
tonumber = [""]

client = vonage.Client(key = api_key, secret = api_secret)
sms = vonage.Sms(client)

def send_message(temp, mintemp, maxtemp, humidity, wind_speed, wind_direction, weather_code):
    for i in tonumber:
        n = tonumber.index(i)
        responseData = sms.send_message(
            {
                "from": "18332746038",
                "to": tonumber[n],
                "text": (f'Current Condition: {weather_code} \nTemperature: {temp}C \nMinimum Temperature: {mintemp}C \nMaximum Temperature: {maxtemp}C \n'
                         f'Humidity: {humidity}% \nWind Speed: {wind_speed} Mph \nWind Direction: {wind_direction}\n'),
            }
        )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
