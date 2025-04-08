# Install these first if not already installed:
# pip install folium geopy

import folium
from geopy.geocoders import Nominatim

# Step 1: Create a geolocator object
geolocator = Nominatim(user_agent="my_geocoder_app")

# Step 2: Ask the user for an address
address = input("Enter an address to map: ")

# Step 3: Geocode the address to get latitude and longitude
location = geolocator.geocode(address)

# Step 4: Handle cases where the address is not found
if location:
    lat, lon = location.latitude, location.longitude
else:
    print("Address not found. Defaulting to White House.")
    lat, lon = 38.8977, -77.0365  # White House coordinates

# Step 5: Create the map
m = folium.Map(location=[lat, lon], zoom_start=15)

# Step 6: Add a marker to the map
folium.Marker(
    location=[lat, lon],
    popup=f"{address}",
    icon=folium.Icon(color="blue")
).add_to(m)

# Step 7: Save the map as an HTML file
m.save("map.html")
print("✅ Map has been saved to map.html. Open it in your browser to view.")
