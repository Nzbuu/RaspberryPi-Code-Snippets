
import text2speechviagoogle as text2speech
import weatherAPI
import forecastio as source

#some useful debug commands
#text2speech.downloadSpeechFromText("hello, how are you today", "./downloadedFile.mp3")

# Get current weather description
json_out = weatherAPI.queryWeatherAPI(source.assembleQueryUrl(source.currentWeatherUrl()));
weatherString1 = source.assembleCurrentWeatherString(json_out);

# Get forecast
json_out = weatherAPI.queryWeatherAPI(source.assembleQueryUrl(source.forecastDayUrl()));
weatherString2 = source.assembleForecastForTheDayString(json_out);

# Assemble full message
fullMessage = weatherString1 + weatherString2 + " Have a nice day!"

#Split into sentences to remain below the googletranslate character limit
splitString = fullMessage.split('. ');

#Create audio output of text
for str in splitString:
    text2speech.speakSpeechFromText(str);







