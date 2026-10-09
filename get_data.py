import json
import requests

# 糸魚川市沖（気象庁JMAモデル）にアドレスを変更してブロックを完全回避
url = "https://open-meteo.com"

print("APIへリクエスト中...")
try:
    response = requests.get(url, timeout=15)
    print(f"サーバーからの返事コード: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        with open("marine_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("【大成功】気象データを正常に保存しました！")
    else:
        print(f"【サーバーエラー】拒否されました。コード: {response.status_code}")
        exit(1)

except Exception as e:
    print(f"【通信エラー】接続に失敗しました。原因: {e}")
    exit(1)
