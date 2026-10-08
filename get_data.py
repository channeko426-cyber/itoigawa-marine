import json
import os
import requests

# 糸魚川市沖の緯度・経度
latitude = 37.22
longitude = 137.86

url = f"https://open-meteo.com{latitude}&longitude={longitude}&hourly=wave_height,wave_direction,wind_wave_height&forecast_days=2"

print(f"URLにアクセス中: {url}")
response = requests.get(url)

if response.status_code == 200:
    try:
        json_data = response.json()
        
        # 【重要】GitHubActionsが確実にファイルを見つけられる場所（現在のフォルダ絶対パス）を計算
        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(current_dir, "marine_data.json")
        
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            
        print(f"Success: ファイルを次の場所に保存しました -> {save_path}")
    except Exception as e:
        print(f"JSON解析エラー: {e}")
else:
    print(f"APIエラー: {response.status_code}")
