import json
import requests

# 糸魚川市沖の緯度・経度
url = "https://open-meteo.com"

print("APIへリクエスト中...")
response = requests.get(url)

if response.status_code == 200:
    # 取得したデータをそのまま書き出す
    with open("marine_data.json", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("保存に成功しました！")
else:
    print(f"APIがエラーを返しました: {response.status_code}")
    exit(1)
