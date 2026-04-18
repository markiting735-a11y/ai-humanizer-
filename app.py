
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
                model="llama-3.1-8b-instant",
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
      
