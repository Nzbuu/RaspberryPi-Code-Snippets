import requests

def currentWeatherUrl():
    queryUrl = 'http://api.openweathermap.org/data/2.5/weather?q=Stevenage,uk&APPID='
    return queryUrl

def forecastDayUrl():
    queryUrl = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Stevenage,uk&mode=json&cnt=1&units=metric&APPID='
    return queryUrl    

def queryWeatherAPI(queryUrl):
    # Load the API key from file
    f = open('myApiKey', 'r');
    apiText = f.read();
    f.close();
    # remove line break
    apiText.rstrip();
    queryUrl = queryUrl + apiText
    response = requests.get(queryUrl);
    json_out = response.json;
    return json_out

def assembleCurrentWeatherString(json_out):
	location = json_out['name'];
	weather  = json_out['weather'][0]['description'];
	weatherString = "The weather in " + location + " right now is " + weather + ". " 
	return weatherString

def assembleForecastForTheDayString(json_out):
    temperature_min = str(json_out['list'][0]['temp']['min']);
    temperature_max = str(json_out['list'][0]['temp']['max']);
    rain_chance     = str(json_out['list'][0]['rain']);
    rain_chance     = str(round(float(rain_chance) * 100));
    wind_speed      = str(json_out['list'][0]['speed']);
    weatherString = "The minimum temperature will be " +  temperature_min + " degrees. " \
    "the maximum will be " + temperature_max + ". The chance of rain is " + rain_chance + " percent. " \
    "The wind speed is " + wind_speed + " meters per second. "
    return weatherString