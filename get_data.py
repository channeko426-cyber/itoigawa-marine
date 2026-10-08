import json
import requests

# 糸魚川市沖（しっかり海上になるポイント）の緯度・経度
LAT = 37.22
LON = 137.86

# 緯度・経度を指定して48時間先までのデータを取得
url = (
    f"https://open-meteo.com"
    f"?latitude={LAT}&longitude={LON}"
    f"&hourly=wave_height,wave_direction,wind_wave_height"
    f"&forecast_days=2"
)

print(f"URLにアクセス中: {url}")
response = requests.get(url)

# サーバーから正常な返事（200）が来たかチェック
if response.status_code == 200:
    try:
        # JSONとして正しく解析できるかテスト
        json_data = response.json()
        with open("marine_data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print("データの保存に成功しました！")
    except Exception as e:
        print(f"JSONの解析エラーが発生しました: {e}")
        print(f"返ってきた中身: {response.text}")
else:
    print(f"APIサーバーがエラーを返しました。ステータスコード: {response.status_code}")
    print(f"エラー内容: {response.text}")
