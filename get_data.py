import json
import requests

# 糸魚川市沖の緯度・経度
latitude = 37.22
longitude = 137.86

# 確実にデータが取得できるURLの組み立て
url = f"https://open-meteo.com{latitude}&longitude={longitude}&hourly=wave_height,wave_direction,wind_wave_height&forecast_days=2"

print(f"URLにアクセス中: {url}")
response = requests.get(url)

if response.status_code == 200:
    try:
        json_data = response.json()
        # 取得したデータを保存
        with open("marine_data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print("Success: marine_data.json を新規作成・保存しました。")
    except Exception as e:
        print(f"JSON解析エラー: {e}")
else:
    print(f"APIエラー: {response.status_code}")
