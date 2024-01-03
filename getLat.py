import requests
from getAuth import getToken
import folium
import testMap
from testMap import drawLineInMap, m, shadeRegions

def runFunction(location, destination):
    #gets coords of the entered location
    urlLocation = "https://www.mapquestapi.com/geocoding/v1/address?key=dSY1U3y1ds3wy5jkNLVrMZjntR2B9ooe&location={}".format(location)
    responseLocation = requests.request("GET", urlLocation)
    dataLocation = responseLocation.json()
    latLocation, lngLotation = dataLocation['results'][0]['locations'][0]['displayLatLng']['lat'], dataLocation['results'][0]['locations'][0]['displayLatLng']['lng']


    #gets coords of the entered destination
    urlDestination = "https://www.mapquestapi.com/geocoding/v1/address?key=dSY1U3y1ds3wy5jkNLVrMZjntR2B9ooe&location={}".format(destination)
    responseDestination = requests.request("GET", urlDestination)
    dataDestination = responseDestination.json()
    latDestination, lngDestination = dataDestination['results'][0]['locations'][0]['displayLatLng']['lat'], dataDestination['results'][0]['locations'][0]['displayLatLng']['lng']

    token = getToken()

    headers = {
    'Authorization': 'Bearer ' + token
    }

    urlfindRoute = f'https://api.iq.inrix.com/findRoute?wp_1={latLocation}%2C{lngLotation}&wp_2={latDestination}%2C{lngDestination}&format=json&routeOutputFields=B,M,P,S,W&maxAlternates=2&RoutingType=Traffic&IsAmbiguousOrigin=true'

    responseFindRoute = requests.request("GET", urlfindRoute, headers=headers)
    route = responseFindRoute.json()

    shadeRegions()

    drawLineInMap(0, 'purple', (latLocation, lngLotation), (latDestination, lngDestination), route)
    drawLineInMap(1, 'black', (latLocation, lngLotation), (latDestination, lngDestination), route)
    drawLineInMap(2, 'blue', (latLocation, lngLotation), (latDestination, lngDestination), route)

    folium.LayerControl().add_to(m)

    m