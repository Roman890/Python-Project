import pyowm

owm = pyowm.OWM('37c9cd8d9a0ab92fe4fb0394c4cc4d76',language='ru')
city = ("Dubai")
observation = owm.weather_at_place(city)

w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp'] # температура
wind = w.get_wind() #ветер
humidity = w.get_humidity() #влажность
print("Погода " + str(w))
print("Температура " + str(round(temperature)))
print("Влажность " + str(humidity))
print("Ветер " + str(wind))
print("Также " + w.get_detailed_status())