import weatherAPI as w

def currentWeatherUrl():
    queryUrl = 'https://api.forecast.io/forecast/'
    return queryUrl

def forecastDayUrl():
    # the current weather forecast contains all the information neede
    queryUrl = currentWeatherUrl();
    return queryUrl   

def assembleQueryUrl(url):
    queryUrl = w.appendAPIKeyToUrl(url, 'forecastio');
    queryUrl = appendLocation(queryUrl);
    queryUrl = queryUrl + "?exclude=minutely,flags&units=si";
    return queryUrl


def assembleCurrentWeatherString(json_out):
    location = 'Stevenage';
    weather  = json_out['currently']['summary'];
    precipitation = str(int(json_out['currently']['precipProbability']));
    weatherString = "The weather in " + location + " right now is " + weather + ". " \
    "The chance of rain is " + precipitation + " percent."
    return weatherString

def assembleForecastForTheDayString(json_out):
    hourlyData = json_out['hourly']['data'];

    # extract minimum and maximum temperature
    temperature = [x['temperature'] for x in hourlyData];
    temperature_min = str(int(min(temperature)));
    temperature_max = str(int(max(temperature)));

    # extract maximum precipitation probablilty
    precipProbability = [x['precipProbability'] for x in hourlyData];
    precipProbability = str(int(max(precipProbability)));

    weatherString = "The minimum temperature will be " +  temperature_min + " degrees. " \
    "the maximum will be " + temperature_max + ". The maximum chance of rain today is " + \
     precipProbability + " percent. "
    return weatherString  

def getLocation():
    class Location(object):
        lattitude = 0
        longitude = 0

    myLocation = Location();
    myLocation.lattitude = 51.9;
    myLocation.longitude = 0.2;
    return myLocation

def appendLocation(url): 
    location = getLocation();
    url = url + "/" +  str(location.lattitude) + ", " + str(location.longitude);
    return url  