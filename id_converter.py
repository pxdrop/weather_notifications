
id_codes = [200, 201, 210, 211, 212, 221, 230, 231, 232, 300, 301, 302, 310, 311, 312, 313, 314, 321, 500, 501, 502,
            503, 504, 511, 520, 521, 522, 531, 600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622, 701, 711, 721,
            731, 741, 751, 761, 762, 771, 781, 800, 801, 802, 803, 804]

weather_codes = ['Thunderstorm', 'Thunderstorm', 'Thunderstorm', 'Thunderstorm', 'Thunderstorm', 'Thunderstorm',
           'Thunderstorm', 'Thunderstorm', 'Thunderstorm', 'Drizzle', 'Drizzle', 'Drizzle', 'Drizzle', 'Drizzle',
           'Drizzle', 'Drizzle', 'Drizzle', 'Drizzle', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain', 'Rain',
           'Rain', 'Rain', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow', 'Snow',
           'Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Dust', 'Ash', 'Squall', 'Tornado', 'Clear', 'Clouds',
           'Clouds', 'Clouds', 'Clouds']

def idconverter(id):
    index = id_codes.index(id)
    weather_name = weather_codes[index]
    return weather_name
