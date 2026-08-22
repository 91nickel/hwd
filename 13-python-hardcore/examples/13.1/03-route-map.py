# pip install folium requests

import folium, requests

start_query = "Москва, Охотный ряд, 2"
end_query   = "Москва, ВДНХ"
profile     = "driving"

def geocode(query: str):
    url    = "https://nominatim.openstreetmap.org/search"
    params = {"q": query, "format": "json", "limit": 1, "accept-language": "ru"}
    r = requests.get(url, params=params, headers={"User-Agent": "colab-student-demo"}, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError(f"Не удалось найти координаты для: {query}")
    return float(data[0]["lat"]), float(data[0]["lon"]), data[0].get("display_name", query)

start_lat, start_lon, _ = geocode(start_query)
end_lat,   end_lon,   _ = geocode(end_query)

r = requests.get(
    f"https://router.project-osrm.org/route/v1/{profile}/{start_lon},{start_lat};{end_lon},{end_lat}",
    params={"overview": "full", "geometries": "geojson", "alternatives": "false", "steps": "false"},
    timeout=20,
)
r.raise_for_status()
route = r.json()
if route.get("code") != "Ok" or not route.get("routes"):
    raise RuntimeError("OSRM не вернул корректный маршрут.")

best         = route["routes"][0]
geom         = best["geometry"]["coordinates"]
distance_km  = best["distance"] / 1000.0
duration_min = best["duration"] / 60.0

m = folium.Map(location=[(start_lat+end_lat)/2, (start_lon+end_lon)/2], zoom_start=12)
folium.GeoJson(
    {"type": "Feature", "geometry": {"type": "LineString", "coordinates": geom}},
    tooltip=f"~{distance_km:.1f} км, ~{duration_min:.0f} мин",
    style_function=lambda x: {"weight": 5, "opacity": 0.9},
).add_to(m)

lats = [start_lat, end_lat] + [lat for _, lat in geom]
lons = [start_lon, end_lon] + [lon for lon, _ in geom]
m.fit_bounds([[min(lats), min(lons)], [max(lats), max(lons)]])
m.save("route.html")
print("Карта сохранена в route.html")
