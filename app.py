import streamlit as st
from groq import Groq
import random

# 1. Page Config
st.set_page_config(page_title="Abubakar's Ghostwriter V8", page_icon="🖋️", layout="wide")

# CSS: Book Editor Theme
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1a1a1a !important; }
    .result-box {
        background-color: #ffffff; color: #1a1a1a; padding: 35px; border-radius: 5px;
        border: 1px solid #ccc; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 18px; box-shadow: 10px 10px 0px #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🖋️ Abubakar's Ghostwriter (V8.0 - Professional Stealth)")
st.caption("Focus: High Burstiness & Low Predictability | KDP Optimized")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original AI Text Yahan Dalein:", height=200)

# 4. The "Ghostwriter" Prompt (Mixing Perplexity & Burstiness)
ghost_prompt = """You are a professional human novelist. Rewrite the user text to be 100% human-passing.
CRITICAL RULES:
1. MAXIMIZE BURSTINESS: Mix extremely short sentences (2-4 words) with very long, descriptive ones (25+ words). 
2. HIGH PERPLEXITY: Use unexpected word choices. Instead of 'he was scared', use 'his pulse thrashed'. Avoid common AI transition words (However, Therefore, Moreover).
3. SENSORY DEPTH: Focus on visceral human reactions—cold sweat, dry mouth, the itch on the skin. 
4. BREAK THE RHYTHM: Use em-dashes (—) and ellipses (...) to interrupt thoughts mid-sentence. 
5. NO REPETITION: If you mention a 'flashlight' once, call it 'the beam' or 'the plastic torch' the next time. 
6. PROFESSIONAL BUT RAW: Keep it high quality for a book, but make the flow unpredictable like a real human's thoughts."""

if st.button("✨ Humanize & Polish"):
    if user_text:
        with st.spinner('Applying Human Texture...'):
            try:
                # High temp for high perplexity (unpredictability)
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "system", "content": ghost_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.35,
                    top_p=0.9
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Professional Book Result:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
                
