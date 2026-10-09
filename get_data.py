import json
import requests

# 2026年最新のOpen-MeteoマリンAPIの正しい接続URL
# 糸魚川市沖（北緯37.22、東経137.86）の波の高さ、波の向き、風速、風向を指定
url = "https://open-meteo.com"

print("最新の気象データサーバーへアクセス中...")
try:
    response = requests.get(url, timeout=15)
    print(f"サーバーの応答コード: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        
        # 【超重要】中身に本当に「波のデータ（hourly）」が入っているか厳重に確認
        if "hourly" in data and "wave_height" in data["hourly"]:
            with open("marine_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("【大成功】本物の最新データを marine_data.json に保存しました！")
        else:
            print("エラー: サーバーから返ってきたデータの形が異常です。保存を中止します。")
            exit(1)
    else:
        print(f"【サーバー拒否】データが取得できませんでした。エラー内容: {response.text}")
        exit(1)

except Exception as e:
    print(f"【通信エラー】気象サーバーへの接続に失敗しました。原因: {e}")
    exit(1)
