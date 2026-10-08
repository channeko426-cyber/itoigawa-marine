import json
import requests

# 糸魚川周辺の範囲を設定 (南端, 西端, 北端, 東端)
LAT_MIN, LON_MIN = 37.0, 137.6
LAT_MAX, LON_MAX = 37.3, 138.1

url = (
    f"https://open-meteo.com"
    f"?hourly=wave_height,wave_direction,wind_wave_height"
    f"&latitude={LAT_MIN}&longitude={LON_MIN}"
    f"&upper_latitude={LAT_MAX}&upper_longitude={LON_MAX}"
    f"&forecast_days=2"
)

response = requests.get(url)
if response.status_code == 200:
    with open("marine_data.json", "w", encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    print("Success")
else:
    print("Failed")
