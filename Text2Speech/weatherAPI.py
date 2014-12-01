import requests

def queryWeatherAPI(url):
    response = requests.get(url);
    json_out = response.json;
    return json_out

def getAPIKey(keyString):
    if keyString == 'openweather':
        f = open('openweathermapAPIKey', 'r');
    elif keyString == 'forecastio':
        f = open('forecastioAPIKey', 'r');
    else:
        print('Invalid key. Use openweathermap or forecastio')
        
    apiText = f.read();
    f.close();
    # remove line break
    apiText = apiText.rstrip();
    return  apiText 

def appendAPIKeyToUrl(url, keyString):
    apiText = getAPIKey(keyString);
    queryUrl = url + apiText; 
    return queryUrl  