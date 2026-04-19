from google import genai
import os
from dotenv import load_dotenv

# .env を読み込む
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# クライアント作成
client = genai.Client(api_key=api_key)

print("--- 利用可能なモデル一覧 ---")
# モデルリストを取得して表示
for model in client.models.list():
    print(f"モデル名: {model.name}")