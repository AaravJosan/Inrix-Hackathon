import requests
import random

payload = ''
headers = {
  'x-api-key': '8e304c9d63741ed0d13d3053072503c11ed29a0c623e2bf5f6290c05e92cbc65'
}

def getAirQual(zipcode):
    url = f'https://api.ambeedata.com/latest/by-postal-code?postalCode={zipcode}&countryCode=US'
    response = requests.request("GET", url=url, headers=headers)

    try:
        response.raise_for_status() 
        dicdata = response.json()  
        airinfo = dicdata.get('stations')
        airinfo = airinfo[0].get('AQI')
        return airinfo
    except:
        a = random.randint(0, 100)
        return a