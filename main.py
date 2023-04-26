#Create an application using the Google Maps API that can calculate distance between any two given locations,

import os
import googlemaps


from dotenv import load_dotenv
load_dotenv()
key = os.getenv('key')

gmaps = googlemaps.Client(key=key)

location_1 = input('Please type in starting town/postcode ')
location_2 = input('Please type in destination town/postcode ')

#print((gmaps.distance_matrix(location_1, location_2)))

#Ask user for input until both addressess are valid
while True:
    response = gmaps.distance_matrix(location_1, location_2)
    if response['rows'][0]['elements'][0]['status'] == 'NOT_FOUND':
        if response['origin_addresses'] == [""]:
            location_1 = input('Please type in valid starting town/postcode ')
        if response['destination_addresses'] == [""]:
            location_2 = input('Please type in valid destination town/postcode ')
    else:
        break
#Ask user to put in appropriate mode of travel string
method_of_travel = input('Please input your mode of travel: “driving”, “walking”, “transit” or “bicycling” ').lower()

while True:
    if method_of_travel in ['driving', 'walking', 'transit' , 'bicycling']:
        response = (gmaps.distance_matrix(location_1, location_2, method_of_travel))
        print(response['rows'][0]['elements'][0]['distance']['text'])
        break
    else:
        method_of_travel = input('Your selection was invalid, please input your mode of travel: “driving”, “walking”, “transit” or “bicycling” ').lower()



