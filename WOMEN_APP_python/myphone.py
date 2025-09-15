import phonenumbers
import folium
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

number = "6379613654"  # Your phone number
region = "IN"  # Assuming this is an Indian number

# Parse phone number
pepnumber = phonenumbers.parse(number, region)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Dynamically construct location query
dynamic_location_query = f"{location}, Tamil Nadu, India"

# Geocoding with OpenCage Geocode
key = "aaa320a4296d42e68fc77b6aa7f94ea6"
geocoder = OpenCageGeocode(key)
results = geocoder.geocode(dynamic_location_query)

if results and len(results):
    lat = results[0]['geometry']['lat'] 
    lng = results[0]['geometry']['lng'] 
    print(f"Location: {location}, Coordinates: {lat}, {lng}")

    # Generate map
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)
    myMap.save("mylocation.html")
else:
    print("Geocoding error: No results found.")
