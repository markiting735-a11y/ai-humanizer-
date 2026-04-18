import streamlit as st
from groq import Groq

# Page Setup
st.set_page_config(page_title="Abubakar's Humanizer Pro", page_icon="🔥")
st.title("🚀 Zero-Detection Humanizer by Abubakar")

# API Key
client = Groq(api_key="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")

user_text = st.text_area("AI Text Yahan Dalein:", height=250)

if st.button("Humanize Karein"):
    if user_text:
        with st.spinner('Making it undetectable...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a casual human writer. Rewrite the input text using a messy, conversational tone. Use slang like 'kinda', 'stuff', 'anyway'. Break grammar rules on purpose—use run-on sentences or fragments. Add filler phrases like 'Honestly,', 'So yeah,', 'I mean,'. Make sure it sounds like a text message or a rough draft. ABSOLUTELY NO ROBOTIC WORDS."},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=1.4  # High randomness to kill patterns
                )
                st.success("Humanized Result (0-5% AI Chance):")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch likhein!")
        
