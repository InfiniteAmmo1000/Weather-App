import requests
import json

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

country = input("Select a country to view the weather: ")
city = input("Select a city to view the weather: ")

querystring = {"q":f"{city},{country}"}

headers = {
	"X-RapidAPI-Key": "6de9a1dc5emsh504f7b004e21483p11742bjsn174d559156d1",
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

text_response = json.loads(response.text)

main = text_response["list"][0]["main"]
weather = text_response["list"][0]["weather"]
wind = text_response["list"][0]["wind"]

def convert_temp(temp):
	new_temp = round(((temp -273.15) * (9/5) + 32), 2)
	return(new_temp)0
data = {
	"city": city.title(),
	"sky": weather[0]["description"],
	"temp": f"{convert_temp(main['temp'])}° F",
	"high": f"{convert_temp(main['temp_max'])}° F",
	"low": f"{convert_temp(main['temp_min'])}° F",
	"wind speed": f"{wind['speed']} mph",
	"wind gust": f"{wind['gust']} mph"
}

for key, value in data.items():
	print(f"{key.title()}, {value}")
