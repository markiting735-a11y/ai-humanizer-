import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Final Wall V14", page_icon="🛡️", layout="wide")

# CSS: High-End Ghost Writer Interface
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; color: #f0f0f0 !important; background-color: #0e1117 !important; border: 1px solid #3d444d; }
    .result-box {
        background-color: #ffffff; color: #000000; padding: 45px; border-radius: 2px;
        border-top: 15px solid #000000; font-family: 'Times New Roman', serif; white-space: pre-wrap;
        line-height: 1.7; font-size: 21px; box-shadow: 20px 20px 60px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ The Final Wall V14.0 (The Untouchable)")
st.caption("Strategy: Forced Imperfection | Sensory Grit | Jitter Logic")

# 2. API Key
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("Original Content (AI/Raw):", height=200, placeholder="Paste your 99% AI text here...")

# 4. The "Glitch-Author" Prompt
# Is prompt mein humne AI ko 'Ghalat' likhne ka order diya hai taky wo 'Human' lagay.
final_wall_prompt = """You are a human writer who is physically terrified while writing this.
Your task: Rewrite the text to bypass AI detectors with a 0% score. 

CRITICAL PROTOCOLS:
1. TOTAL BAN ON AI GLOSSARY: Never use: 'Symphony', 'Tapestry', 'Testament', 'Dance', 'Echo', 'Embrace', 'Shrouded', 'Whisper', 'Shadows', 'Labyrinth'. Use blunt, ugly words.
2. THE 'JITTER' RHYTHM: Write like a person who can't catch their breath. Use fragments. 
   - Rule: One very short sentence (3 words). One very long, messy sentence (35 words). One medium sentence. Repeat.
3. PHYSICAL GRIT: Focus only on the body. The taste of copper in the mouth. Sweat stinging the eyes. The smell of old, wet cardboard. 
4. NO FLOW: AI flows too well. You must break the flow. Jump between ideas without using 'But', 'So', 'However', or 'Then'.
5. ACTIVE & RAW: Instead of 'He was gripped by fear', say 'His heart tried to kick its way out of his chest.'
6. NO ADVERBS: Remove 'Slowly', 'Quickly', 'Quietly'. Show the action without the -ly words."""

if st.button("🔥 Destroy AI Footprint"):
    if user_text:
        with st.spinner('Applying Jitter Logic...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": final_wall_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.45, # Maximum randomness to break mathematical patterns
                    top_p=0.8
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Human-Grade Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Raw Copy for KDP:**")
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kachra dalo tabhi toh saaf karunga!")

st.markdown("---")
st.caption("Developed for Abubakar | V14.0 Elite Bypass Engine")
