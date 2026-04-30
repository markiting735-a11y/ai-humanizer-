import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Cinema Studio", page_icon="🎬", layout="wide")

# CSS: Professional Midnight Theme
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1a1a1a !important; }
    .result-box {
        background-color: #f9f9f9; color: #111111; padding: 35px; border-radius: 5px;
        border-left: 8px solid #d32f2f; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 19px; box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Abubakar's Cinema Studio (V10.0 - Premium Quality)")
st.caption("Mode: Cinematic Storytelling | Anti-AI Math Logic")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original Story Draft Yahan Dalein:", height=200)

# 4. The "Cinematic Human" Prompt
cinema_prompt = """You are a high-end thriller novelist like Stephen King. 
Rewrite the text to be professional, gripping, and 100% human-passing.

RULES TO BEAT DETECTORS & WIN READERS:
1. NO CLICHES: Don't say 'he was terrified'. Describe his heartbeat hitting his teeth. 
2. VARY RHYTHM: Use short, punchy action lines followed by one long, flowing sensory description. 
3. HUMAN GRIT: Use words that feel heavy or sharp (e.g., 'grime', 'slick', 'stabbing', 'hollow'). 
4. NO 'AI' CONNECTORS: Never use 'Suddenly', 'However', 'Moreover'. Just jump into the action.
5. DEEP POV: Stay inside the character's head. If he's scared, the whole world should look distorted.
6. THE 'GLITCH': Use em-dashes (—) and fragments. It breaks the AI's mathematical flow."""

if st.button("🔥 Create Masterpiece"):
    if user_text:
        with st.spinner('Writing like a pro...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-70b-versatile", # Using a bigger model for better quality
                    messages=[{"role": "system", "content": cinema_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.2,
                    top_p=0.9
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Book-Ready Content:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
                
