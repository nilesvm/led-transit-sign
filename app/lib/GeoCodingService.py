import urllib.request, json
# from app import app.config

class GeoCodingService():

  def __init__(self, location):
    # must be string with street, city, state, zip
    self.location = location
    self.googlemaps_key = 'AIzaSyD5pNwbBpfiOLX5yV2PkwSmGjsqblR2KDw'
    # self.googlemaps_key = app.config['GOOGLEMAPS_KEY']

  def get_coordinates(self):
    raw_coordinates = self.request()['results'][0]['geometry']['location']
    coordinates = { 'latitude': raw_coordinates['lat'], 'longitude': raw_coordinates['lng'] }
    return coordinates

  def request(self):
    response = urllib.request.urlopen(self.request_url())
    # Google API returns JSON
    decode = response.info().get_param('charset') or 'utf-8'
    data = json.loads(response.read().decode(decode))
    return data

  def request_url(self):
    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

    google_root = "https://maps.googleapis.com/maps/api/geocode/json?"
    return google_root + self.location_string() + self.googlemaps_key_string()

  def googlemaps_key_string(self):
    return "&key="+ self.googlemaps_key

  def location_string(self):
    return "address=" + self.location



