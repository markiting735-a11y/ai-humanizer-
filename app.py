import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Humanizer 🔥Pro", page_icon="🚀", layout="wide")

# CSS: Professional look with clean wrapping
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117; color: #e0e0e0; padding: 25px; border-radius: 12px;
        border: 1.5px solid #4b4b4b; font-family: 'Georgia', serif; white-space: pre-wrap;
        margin-top: 15px; margin-bottom: 15px; line-height: 1.8; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")
st.caption("PRO-STEALTH MODE: Professional Flow with Zero AI Footprint")

# 2. API Key Setup
client = Groq(api_key="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")

st.subheader("⚙️ Configuration")
mood = st.selectbox("Style Select Karein:", 
                    ["Professional Novelist (KDP Ready)", "Deep Human (Raw & Emotional)"])

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karein:", height=250, placeholder="Write your chapter here...")

# 4. Optimized Logic for Professional Stealth
if mood == "Professional Novelist (KDP Ready)":
    # Is prompt mein 'typos' hata diye hain aur 'flow' par zor diya hai
    system_prompt = """You are a highly skilled, award-winning human author. 
    Your goal is to rewrite the text to be 100% human-passing while maintaining professional publishing standards.
    
    RULES FOR PROFESSIONAL STEALTH:
    1. VARY SENTENCE LENGTH: Mix very short, punchy sentences with long, descriptive ones. (This destroys AI patterns).
    2. NO HEADINGS: Write in continuous, flowing paragraphs only. 
    3. COMPLETE WORDS ONLY: Do not use typos, do not cut words, and do not use brackets like (sigh).
    4. SHOW, DON'T TELL: Instead of saying someone is scared, describe their cold sweat or trembling hands.
    5. NATURAL TRANSITIONS: Use human-like transitions (e.g., 'And yet', 'Then again', 'Truth be told').
    6. FORBIDDEN AI WORDS: Never use 'delve', 'tapestry', 'testament', 'vibrant', 'comprehensive', or 'embody'."""
    
    # Temperature ko 0.9-1.1 ke beech rakha hai (Stability + Creativity)
    base_temp = 0.95 + random.uniform(0.01, 0.1)
else:
    system_prompt = """You are a rebellious human storyteller. Write with raw emotion. 
    Use sentence fragments. Start sentences with 'But' or 'Because'. 
    Make the rhythm jagged and unpredictable. Sound like a real person with a soul, not a machine."""
    base_temp = 1.25 + random.uniform(0.01, 0.1)

# 5. Process Button
if st.button("✨ Humanize & Professionalize"):
    if user_text:
        with st.spinner('Crafting a masterpiece...'):
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
                st.subheader("✅ Professional Humanized Content:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Copy for KDP/Word:**")
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle text toh dalo!")
        
