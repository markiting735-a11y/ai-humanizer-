
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
                    {"role": "system", "content": "You are a human writer with a unique, slightly imperfect style. Rewrite the text using 'Burstiness' (mix of short and long sentences) and 'Perplexity' (uncommon word choices). Use a conversational tone, include occasional idioms, and avoid standard AI transition words like 'Furthermore' or 'Moreover'. Make it sound like a personal story, not a machine-generated summary."},
                    {"role": "user", "content": user_text}
                ],
                temperature=1.0
            )
            st.success("Humanized Result:")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Pehle kuch likhein!")
      
