import json
import requests

# 糸魚川市沖の緯度・経度
url = "https://open-meteo.com"

print("APIへリクエスト中...")
response = requests.get(url)

if response.status_code == 200:
    try:
        # 返ってきた中身が正しいJSONデータか厳重にチェック
        data = response.json()
        if "hourly" in data:
            with open("marine_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("【大成功】正しい気象データを marine_data.json に保存しました！")
        else:
            print("エラー: データの形が異常です")
            exit(1)
    except Exception as e:
        print(f"JSON変換エラー: {e}")
        exit(1)
else:
    print(f"APIエラー: {response.status_code}")
    exit(1)
