from geopy.distance import geodesic

TokyoStation = (35.681382, 139.76608399999998)
NagoyaStation = (35.170915, 136.881537)

dia = geodesic(TokyoStation, NagoyaStation).km

print(dia)