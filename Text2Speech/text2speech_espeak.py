import  sys
import pyttsx
import weatherAPI


    # main() function
def main():
    # use sys.argv if needed
    print 'running speech-test.py...'
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.setProperty('voice', 'english')

    json_out = weatherAPI.queryWeatherAPI(weatherAPI.currentWeatherUrl());
    str1 = weatherAPI.assembleCurrentWeatherString(json_out);

    json_out = weatherAPI.queryWeatherAPI(weatherAPI.forecastDayUrl());
    str2 = weatherAPI.assembleForecastForTheDayString(json_out);

    fullMessage = str1 + str2 +  "Have a nice day!";

    splitString = fullMessage.split('. ');
     
    for str in splitString:
        print(str)
        engine.say(str)
        engine.runAndWait()

# call main
if __name__ == '__main__':
  main()

