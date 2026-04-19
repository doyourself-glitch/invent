import os
from dotenv import load_dotenv
from google import genai  # 新しいライブラリの読み込み方

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print("--- 新ライブラリで接続テスト開始 ---")

try:
    # クライアントの作成（新仕様）
    client = genai.Client(api_key=api_key)
    
    print("モデル呼び出し中...")
    
    # モデルへのリクエスト（新仕様）
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="こんにちは、テストです",
    )
    
    print("---------------------------------")
    print("成功！API接続バッチリです！")
    print("AIからの返事:", response.text)
    print("---------------------------------")

except Exception as e:
    print("---------------------------------")
    print("【エラー発生】")
    print(e)
    print("---------------------------------")