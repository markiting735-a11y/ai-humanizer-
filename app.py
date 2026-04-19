import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Humanizer 🔥Pro", page_icon="🚀", layout="wide")

# CSS: Mobile friendly UI aur Text Wrap fix
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117;
        color: #e0e0e0;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #ff4b4b;
        font-family: 'Georgia', serif;
        white-space: pre-wrap;
        margin-top: 15px;
        margin-bottom: 15px;
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")
st.caption("ULTRA-STEALTH MODE: Designed for Zero AI Detection")

# 2. API Key Setup
client = Groq(api_key="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")

st.subheader("⚙️ Configuration")
mood = st.selectbox("Style Select Karein:", 
                    ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karein:", height=250, placeholder="Write your chapter here...")

# 4. Chaos & Randomization Logic
random_factor = random.uniform(0.05, 0.25) 

if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a messy human storyteller. Use slang, 'uhm', 'like', 'literally', and occasional typos. Break every rule of writing. Sound like a chaotic person on a voice note."
    base_temp = 1.4 + random_factor
else:
    # ULTRA-HUMAN NOVELIST PROMPT (Anti-Detector)
    system_prompt = """You are a rebellious, emotional human novelist. 
    Your mission: Rewrite the text so it's 100% IMPOSSIBLE to detect as AI.
    
    CRITICAL STRATEGY:
    1. JAGGED RHYTHM: Use 'Burstiness'. Some sentences should be one word. Others should be long and breathless.
    2. HUMAN FLAWS: Start sentences with 'And', 'But', or 'Because'. Use fragments. (e.g., 'A cold night. Too cold.')
    3. SENSORY OVERLOAD: Describe physical sensations—the metallic tang of blood, the itch of a wool sweater, the way a heart stutters.
    4. NO AI WORDS: Strictly ban: 'delve', 'testament', 'labyrinth', 'shrouded', 'unbeknownst', 'intricate', 'multifaceted'.
    5. INTERNAL CHAOS: Use ellipses (...) and dashes (-) to show a character's messy thought process. 
    If a sentence feels too perfect, break it. Sound raw, tired, and real."""
    
    # Temperature high rakha hai taake prediction zero ho jaye
    base_temp = 1.35 + random_factor

# 5. Process Button
if st.button("✨ Humanize & Destroy AI Patterns"):
    if user_text:
        with st.spinner('Evading AI Detectors...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=base_temp
                )
                
                result = response.choices[0].message.content
                
                # Output Section
                st.subheader("✅ Humanized Masterpiece:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Copy from the box below:**")
                st.code(result, language=None)
                
                # Word Counter
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} | 🛡️ Stealth Level: Maximum")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch text toh dalo!")

st.markdown("---")
st.caption("Developed by Abubakar | Author Edition")
