import streamlit as st
import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("GiftCompass")
st.subheader("SNS投稿から、")

sns_post = st.text_area("AIが分析中です")

if st.button("分析する"):
    if sns_post:
        with st.spinner("AIが分析中です"):
            prompt = f"""
            以下のSNS投稿内容を分析し、ユーザーの「隠れ欲求」を推測してください。
            その上で、その人に最適なギフトを１つ提案し、その理由を述べてください。

            『SNS投稿内容』
            {sns_post}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.markdown("---")
            st.markdown(response.text)
    else:
        st.warning("投稿内容を入力してください")