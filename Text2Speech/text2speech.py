#!/usr/bin/env python
# Written in Python, using code blocks written by Martin O'Hanlon, www.stuffaboutcode.com

import json, urllib, subprocess, pycurl, requests


# function to download a file from a url, used for testing
def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

# returns the appropriate google speech url for a particular phrase
def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q': phrase}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

# function to download an mp3 file for a particular phrase, used for testing
def downloadSpeechFromText(phrase, fileName):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    print googleSpeechURL
    downloadFile(googleSpeechURL, fileName)

# output phrase to audio using mplayer
def speakSpeechFromText(phrase):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
    weatherString = "The minimum temperature will be " +  temperature_min + " degrees, " \
    "the maximum will be " + temperature_min + ". The chance of rain is " + rain_chance + "percent," \
    " the wind speed is " + wind_speed + " meters per second."
    return weatherString

#some useful debug commands
#download a speech file from google
#downloadSpeechFromText("hello, how are you today", "./downloadedFile.mp3")
#output phrase to audio
json_out = queryWeatherAPI(currentWeatherUrl());
weatherString1 = assembleCurrentWeatherString(json_out);


json_out = queryWeatherAPI(forecastDayUrl());
weatherString2 = assembleForecastForTheDayString(json_out);

fullMessage = weatherString1 + weatherString2 + " Have a nice day!"
splitString = fullMessage.split('. ');

for str in splitString:
    speakSpeechFromText(str);







