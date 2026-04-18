
import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(page_title="Abubakar's Humanizer", page_icon="✍️")
st.title("🚀 AI to Human Converter creator Abubakar")

# API Key Connection
client = Groq(api_key="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")

user_text = st.text_area("AI Text Yahan Dalein:", height=250)

if st.button("Humanize Karein"):
    if user_text:
        with st.spinner('Thinking like a human...'):
            response = client.chat.completi
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "Rewrite this like a real person sharing a story or info. Use a mix of punchy short sentences and descriptive ones. Avoid typical AI transition words. Throw in a few rhetorical questions and keep the tone conversational, as if you're explaining this to a friend. Make it flow naturally, not like a structured list."},
                    {"role": "user", "content": user_text}
                ],
                temperature=1.3
            )
            st.success("Humanized Result:")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Pehle kuch likhein!")
      
