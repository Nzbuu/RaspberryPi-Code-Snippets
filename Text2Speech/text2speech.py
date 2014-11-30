
import text2speechviagoogle as text2speech
import weatherAPI

#some useful debug commands
#text2speech.downloadSpeechFromText("hello, how are you today", "./downloadedFile.mp3")

# Get current weather description
json_out = weatherAPI.queryWeatherAPI(weatherAPI.currentWeatherUrl());
weatherString1 = weatherAPI.assembleCurrentWeatherString(json_out);

# Get forecast
json_out = weatherAPI.queryWeatherAPI(weatherAPI.forecastDayUrl());
weatherString2 = weatherAPI.assembleForecastForTheDayString(json_out);

# Assemble full message
fullMessage = weatherString1 + weatherString2 + " Have a nice day!"

#Split into sentences to remain below the googletranslate character limit
splitString = fullMessage.split('. ');

#Create audio output of text
for str in splitString:
    text2speech.speakSpeechFromText(str);







