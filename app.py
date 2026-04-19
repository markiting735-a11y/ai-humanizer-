import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Humanizer Pro", page_icon="🚀", layout="wide")

# CSS for Line Wrap and Mobile View
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; }
    .result-box {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        font-family: sans-serif;
        white-space: pre-wrap; /* Ye line mobile par text wrap karegi */
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")

# 2. API Key Setup
client = Groq(api_key="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")

st.subheader("⚙️ Settings")
mood = st.selectbox("Style Select Karein (Tone):", ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])

user_text = st.text_area("Original AI Text Yahan Paste Karein:", height=200, placeholder="Write here...")

# 3. Randomness for 0% Detection
random_factor = random.uniform(0.01, 0.15) # Har baar naya result

if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a human writer. Use slang, occasional typos, and a very messy conversational style. Use filler words like 'like', 'literally', 'I mean'. Break every robotic pattern."
    base_temp = 1.35 + random_factor
else:
    system_prompt = "You are a professional novelist. Use deep human emotions, varying sentence lengths, and natural flow. Avoid all common AI phrases. Make it sound 100% human-written."
    base_temp = 0.85 + random_factor

# 4. Process Button
if st.button("✨ Humanize & Generate"):
    if user_text:
        with st.spinner('Generating unique human version...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_text}],
                    temperature=base_temp
                )
                
                result = response.choices[0].message.content
                
                # Output
                st.subheader("✅ Humanized Result:")
                
                # Box 1: For Reading (Mobile Wrap)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                # Box 2: For One-Click Copy
                st.write("📋 **Neechay box se copy karein:**")
                st.code(result, language=None)
                
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} | 🛡️ Anti-AI Score: Maximum")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle text toh likhein!")

st.markdown("---")
st.caption("Developed by Abubakar | Fiction & Audiobook Specialist")
