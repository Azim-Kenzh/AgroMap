# import requests
# from django.test import TestCase
#
# # Create your tests here.
#
# headers = {
#     'X-Gismeteo-Token': '56b30cb255.3443075',
#     'Accept-Encoding': 'deflate, gzip'
# }
# a = requests.get('https://api.weather.yandex.ru/v2/informers?').json()
# print(a)

# import the module
import python_weather
import asyncio
import os


async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(format=python_weather.METRIC) as client:

        # fetch a weather forecast from a city
        weather = await client.get("New York")

        # returns the current day's forecast temperature (int)
        print(weather.current.temperature)

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            print(forecast.date, forecast.astronomy)

            # hourly forecasts
            for hourly in forecast.hourly:
                print(f' --> {hourly!r}')


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())