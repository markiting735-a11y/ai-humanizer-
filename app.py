import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's V18 Ultra", page_icon="🕵️‍♂️", layout="wide")

# CSS: Dark Ghost Mode
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; color: #f0f0f0 !important; background-color: #0d1117 !important; border: 1px solid #30363d; }
    .result-box {
        background-color: #ffffff; color: #000000; padding: 40px; border-radius: 5px;
        border-top: 20px solid #000000; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 20px; box-shadow: 10px 10px 30px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️‍♂️ Ghost Writer Ultra V18.0")
st.caption("Status: Maximum Stealth | Mode: Human Jitter + Conversational Grit")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original AI Garbage Here:", height=200)

# 4. The "Ghost Ultra" Prompt
# Is prompt mein humne AI ko 'Conversational' aur 'Raw' banne ka order diya hai.
ghost_ultra_prompt = """You are a raw, human storyteller. Your mission is to rewrite the text so that it passes ALL AI detectors (0% score) while being high-quality for readers.

EXECUTION RULES:
1. CONVERSATIONAL JITTER: Use fillers like 'I mean', 'actually', 'sort of', 'maybe'. Human minds wander; AI doesn't.
2. BREAK THE RHYTHM: Follow a long sentence with a 1-word or 2-word sentence. Use em-dashes (—) to cut off thoughts abruptly.
3. BAN AI VOCABULARY: Never use 'tapestry', 'testament', 'labyrinth', 'shrouded', 'echoed', 'miasma'. Use 'Mess', 'Stink', 'Noise', 'Real'.
4. SENSORY GRIT: Focus on 'Body Panic'—the sour taste of bile, the sting of cold sweat in eyes, the ringing in ears.
5. NO REPETITION: If you used 'fear' or 'dark', do not use them again for the next 2 paragraphs. Find new, ugly ways to describe it.
6. NO PATTERNS: Do not start sentences the same way twice. If the last sentence started with 'The', start this one with a verb or a sound."""

if st.button("🔥 Execute Ultra Stealth"):
    if user_text:
        with st.spinner('Scrubbing every machine trace...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": ghost_ultra_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.65, # Very high randomness for human-like choice of words
                    top_p=0.85
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Ghost-Proof Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kachra dalo!")

st.markdown("---")
st.caption("V18.0 Built for Abubakar | No Detection. No Mercy.")
