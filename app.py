
import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(page_title="Abubakar's Humanizer", page_icon="✍️")
st.title("🚀 AI to Human Converter")

# API Key Connection
client = Groq(api_key="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")

user_text = st.text_area("AI Text Yahan Dalein:", height=250)

if st.button("Humanize Karein"):
    if user_text:
        with st.spinner('Thinking like a human...'):
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a professional human writer. Rewrite the text to have high perplexity and burstiness. Use natural flow and avoid common AI words to bypass ZeroGPT perfectly."},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.9
            )
            st.success("Humanized Result:")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Pehle kuch likhein!")
      
