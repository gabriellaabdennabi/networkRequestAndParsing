
import requests
import json


def get_data_and_parse():
    weather_api_url = "https://api.weather.gov/openapi.json"
    data = requests.get(weather_api_url)
    jsonData = json.loads(data.text)

    return jsonData

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data()
    # parse_data(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
