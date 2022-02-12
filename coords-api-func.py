from geopy.geocoders import Nominatim

#pip install geopy

def get_coords(postCode):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(postCode)
    return location.latitude, location.longitude

lat, long = get_coords("G12 8RR")
print(lat)