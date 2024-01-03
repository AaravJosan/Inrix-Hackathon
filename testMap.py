import folium
import json
from getAQI import getAirQual

m = folium.Map(location=(37.7749, -122.4194), zoom_start=13)

def shadeRegions():
    a = open('sf.json', 'r')
    b = a.read()
    data = json.loads(b)

    for i in range(0, 23):
        zipcode = data['features'][i]['properties']['id']
        zipdata = data['features'][i]
        airQuality = getAirQual(zipcode)
        if(airQuality > 40):
            postcodes = folium.GeoJson(zipdata, color = 'red')        
        elif(33 < airQuality < 40):
            postcodes = folium.GeoJson(zipdata, color = 'yellow')
        else:
            postcodes = folium.GeoJson(zipdata, color = 'green')
        postcodes.add_to(m)
    

def drawLineInMap(routeNumber,Color,fromPoint,destinationPoint,route):
  route_coordinates = []
  for coords in route['result']['trip']['routes'][routeNumber]['points']['coordinates'] :
    # print(coords[0])
    route_coordinates.append([(coords[1],coords[0])])
    cleanroute = []
  for location in route_coordinates:
    #print(location[0])
    cleanroute.append(location[0])

  # Add a polyline to the map
  folium.PolyLine(
    locations=cleanroute,
    color=Color,  # Line color
    weight=5,       # Line weight
    opacity=0.7,    # Line opacity
    popup='route '+str(routeNumber),  # Popup text
  ).add_to(m)
  # Example coordinate for a single point
  point_coordinate_From = fromPoint
  point_coordinate_Destination = destinationPoint

  # Change the color of the marker
  marker_color = 'blue'  # Choose your desired color

  folium.Marker(location=point_coordinate_From, popup='Source', icon=folium.Icon(color=marker_color)).add_to(m)
  folium.Marker(location=point_coordinate_Destination, popup='Destination', icon=folium.Icon(color=marker_color)).add_to(m)
