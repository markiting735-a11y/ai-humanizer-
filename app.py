import streamlit as st
from groq import Groq
import random

# 1. Page Configuration (Wide layout for mobile & desktop)
st.set_page_config(page_title="Abubakar's Humanizer Pro", page_icon="🚀", layout="wide")

# CSS: Mobile friendly UI, Line Wrap, aur Professional Look
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117;
        color: #e0e0e0;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #4CAF50;
        font-family: 'Georgia', serif;
        white-space: pre-wrap;
        margin-top: 15px;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")
st.caption("Advanced Humanization Engine for Fiction & Authors")

# 2. API Key Setup
client = Groq(api_key="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")

st.subheader("⚙️ Settings")
mood = st.selectbox("Style Select Karein (Tone):", 
                    ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])

st.markdown("---")

# 3. Input Area
user_text = st.text_area("Original AI Text Yahan Paste Karein:", height=250, placeholder="Apni story ka chapter yahan paste karein...")

# 4. Logic & Randomization (For 0% Detection)
random_factor = random.uniform(0.01, 0.20) 

if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a human writer. Use slang, messy conversational style, filler words (like, literally, I mean), and occasional typos. Break every robotic pattern. Sound like a person telling a story to a friend."
    base_temp = 1.35 + random_factor
else:
    # GOD-LEVEL WRITER PROMPT (Anti-Detector)
    system_prompt = """You are a master human novelist. Rewrite the input to be 100% indistinguishable from human writing.
    
    CRITICAL INSTRUCTIONS:
    1. VARY RHYTHM: Mix very short, punchy sentences with long, descriptive ones. Use fragments.
    2. SHOW, DON'T TELL: Use sensory details (smell, taste, touch, sound). Don't say 'he was scared', say 'his palms were slick with cold sweat'.
    3. INTERNAL VOICE: Include internal thoughts, rhetorical questions, and human-like hesitations.
    4. NO ROBOT WORDS: Absolutely NO: 'delve', 'testament', 'labyrinth', 'multifaceted', 'embark', 'intricate', 'furthermore'.
    5. FLOW: Start some sentences with 'And', 'But', or 'Or'. Use dashes (-) and ellipses (...) to show human thought flow."""
    base_temp = 1.25 + random_factor

# 5. Process Button
if st.button("✨ Humanize & Generate"):
    if user_text:
        with st.spinner('Crafting a unique human masterpiece...'):
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
                st.subheader("✅ Humanized Result:")
                
                # Box 1: Professional Reading View (Wrapped for Mobile)
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                # Box 2: Easy Copy Section
                st.write("📋 **Neechay box ke top-right se copy karein:**")
                st.code(result, language=None)
                
                # Metrics
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} | 🛡️ Detection Shield: Active")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch text toh likhein!")

st.markdown("---")
st.caption("Developed by Abubakar | Perfect for Draft2Digital & KDP")
