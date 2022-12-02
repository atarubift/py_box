import geocoder

location = "フジテレビ"
ret = geocoder.osm(location, timeout=5.0)
print(ret.latlng)