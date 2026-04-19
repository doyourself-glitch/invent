import os
from dotenv import load_dotenv
from google import genai

# .envの設定
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 新しいクライアント設定
client = genai.Client(api_key=api_key)

def analyze_and_suggest(sns_post):
    prompt = f"""
    以下のSNS投稿内容を分析し、ユーザーの「隠れ欲求」を推測してください。
    その上で、その人に最適なギフトを1つ提案し、その理由を述べてください。
    
    思考のステップ(Chain of Thought)を以下の順で行い、そのまま出力してください：
    1. 投稿から読み取れる感情や状況の分析
    2. その背後にある「隠れ欲求」の特定
    3. それを踏まえたギフトの選定理由

    【SNS投稿内容】
    {sns_post}
    
    【出力形式】
    ・AIの思考プロセス
    ・隠れ欲求：
    ・おすすめギフト：
    ・渡す理由：
    """
    
    print("AIが分析中...")
    
    # モデルの呼び出し（最新のgemini-2.5-flashを使用）
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    print("\n--- GiftCompassからの提案 ---\n")
    print(response.text)

if __name__ == "__main__":
    text = input("SNSの投稿内容を入力してください: ")
    analyze_and_suggest(text)