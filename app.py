import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Chaos Studio V7", page_icon="🕵️", layout="wide")

# CSS: Dark Mode UI
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117; color: #dcdcdc; padding: 25px; border-radius: 12px;
        border: 2px solid #ff4b4b; font-family: 'Courier New', monospace; white-space: pre-wrap;
        margin-top: 15px; line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚔️ Abubakar's Chaos Studio (V7.0 - Detection Killer)")
st.caption("Mode: Messy Human Writing | Target: 0% AI Score")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karo:", height=250, placeholder="Paste that 100% AI text here...")

# 4. The "Chaos & Messy" Prompt (Detector Killer)
chaos_prompt = """You are a nervous, uneducated person writing a fast social media post or a messy first draft. 
STRICT RULES TO DESTROY AI PATTERNS:
1. NO PERFECT GRAMMAR: Start sentences with 'And', 'But', 'Cuz', or 'So'. Use '...' frequently.
2. FRAGMENTED THOUGHTS: Use very short, 1-3 word sentences randomly. (Example: 'Dead silence. Scared.')
3. TOTAL RANDOMNESS: One sentence must be long and rambling, the next must be tiny.
4. NO 'AI' WORDS: Never use metaphors like 'shrouded', 'burning lungs', or 'heart thumping like a drum'. 
5. USE FILLERS: Add words like 'honestly', 'basically', 'I mean', 'well'.
6. BREAK THE THIRD PERSON: Occasionally use 'I' or 'Me' as if the narrator is talking to the reader.
7. REWRITE EVERYTHING: Do not keep the original sentence structure. Break it apart."""

if st.button("🔥 Destroy AI Detection"):
    if user_text:
        with st.spinner('Breaking the algorithm...'):
            try:
                # Maximize randomness with high temperature and top_p
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": chaos_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=1.5, # Super high for maximum chaos
                    top_p=0.95
                )
                
                result = response.choices[0].message.content
                
                # Output Section
                st.subheader("✅ Humanized (Chaos Mode):")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Copy for KDP (Apply manual typos for 0% score):**")
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Kuch likho toh sahi!")

st.markdown("---")
st.caption("Developed by Abubakar | Chaos Edition V7")
