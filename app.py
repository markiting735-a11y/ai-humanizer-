import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Chaos Studio", page_icon="💀", layout="wide")

# CSS: Professional but Dark Theme
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117; color: #d0d0d0; padding: 25px; border-radius: 12px;
        border: 2px solid #ff4b4b; font-family: 'Georgia', serif; white-space: pre-wrap;
        margin-top: 15px; line-height: 1.7; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Abubakar's Stealth Studio (V5.0 - The Chaos Update)")
st.caption("Target: 0% AI Detection | Mode: Human Imperfection")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karein:", height=250, placeholder="Paste your 100% AI text here...")

# 4. The Final Anti-Detector Prompt
# Ismein hum AI ko 'Be-waqoof' aur 'Thaka hua' banne ka keh rahe hain
stealth_prompt = """You are a tired, stressed-out human writer writing a first draft. 
Rewrite the user's text to be messy, blunt, and completely UNPREDICTABLE.

STRICT RULES TO KILL AI DETECTION:
1. NO REPETITION: Never mention the same object (like 'fridge' or 'heart') more than twice. 
2. FRAGMENTED THOUGHTS: Use '...' or '-' to show a mind that is jumping between ideas.
3. HUMAN FILLERS: Throw in random human thoughts (e.g., 'I mean', 'Actually', 'It was weird').
4. BURSTINESS: One sentence must be very long (20+ words). The next must be 1-3 words. (Example: 'Darkness.')
5. IMPERFECT GRAMMAR: Start sentences with 'And', 'But', 'So'. Use contractions (don't, it's). 
6. NO AI WORDS: Strictly ban 'shrouded', 'testament', 'vibrant', 'intricate', 'delve', 'tapestry'.
7. RAW TONE: Sound like a person talking on a voice note, not a polished book."""

if st.button("🚀 Break AI Patterns & Humanize"):
    if user_text:
        with st.spinner('Injecting Human Chaos...'):
            try:
                # Randomize params for maximum stealth
                dynamic_temp = random.uniform(1.2, 1.4)
                dynamic_top_p = random.uniform(0.85, 0.95)
                
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": stealth_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=dynamic_temp,
                    top_p=dynamic_top_p
                )
                
                result = response.choices[0].message.content
                
                # Output Section
                st.subheader("✅ Humanized (The 'Messy' Draft):")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Copy for KDP (Then add 2-3 manual typos):**")
                st.code(result, language=None)
                
                st.info("💡 Pro Tip: Is result mein manually 1-2 spelling ghalat kar do, detector 0% ho jayega.")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch dalo toh sahi!")

st.markdown("---")
st.caption("Developed by Abubakar | Author Stealth Edition")
