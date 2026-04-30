import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Stealth Studio", page_icon="🕵️", layout="wide")

# CSS: Clean UI
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117; color: #e0e0e0; padding: 25px; border-radius: 12px;
        border: 2px solid #4CAF50; font-family: 'Courier New', monospace; white-space: pre-wrap;
        margin-top: 15px; line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Abubakar's Stealth Studio (Anti-Detector)")
st.caption("Mode: Pattern Destroyer | Version 4.0")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karein:", height=250, placeholder="Paste your robotic AI text here...")

# 4. The Logic (The Secret Sauce)
# Is prompt mein humne AI ko 'Ghalat' aur 'Raw' hone ka kaha hai
stealth_prompt = """You are a human writer who HATES AI. Rewrite the user's text to destroy all mathematical patterns.

CRITICAL INSTRUCTIONS:
1. VARY SENTENCE LENGTH (THE 'BURSTINESS' RULE): 
   - Make one sentence extremely long and descriptive. 
   - Make the very next sentence only 1 or 2 words long. (Example: 'He looked. Darkness.')
2. NO STARTING PATTERNS: Never start two sentences in a row with the same word (e.g., No 'The... The...', No 'He... He...').
3. USE CASUAL CONNECTORS: Use words like 'Anyway', 'So', 'Well', 'Actually' to break the formal flow.
4. BREAK THE RHYTHM: Use dashes (—) and ellipses (...) to show messy human thoughts. 
5. BE IMPERFECT: Use contractions (don't, won't, can't). If a sentence is too 'poetic', simplify it into raw, blunt English.
6. NO AI WORDS: Ban 'shrouded', 'testament', 'vibrant', 'intricate', 'delve', 'tapestry'."""

if st.button("✨ Destroy AI Patterns & Humanize"):
    if user_text:
        with st.spinner('Breaking the algorithm...'):
            try:
                # Randomize temperature for each run to avoid signature patterns
                dynamic_temp = random.uniform(1.1, 1.3)
                
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": stealth_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=dynamic_temp
                )
                
                result = response.choices[0].message.content
                
                # Output Section
                st.subheader("✅ Humanized (Raw Mode):")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
                st.success("Pattern Broken. Stealth Active.")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Kuch text toh dalo bhai!")

st.markdown("---")
st.caption("Developed by Abubakar | No-Pattern Edition")
