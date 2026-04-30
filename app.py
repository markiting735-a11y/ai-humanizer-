import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's V17 Final Kill", page_icon="🎯", layout="wide")

# CSS: Dark Ghost Interface
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; color: #ffffff !important; background-color: #111111 !important; border: 2px solid #333; }
    .result-box {
        background-color: #fcfcfc; color: #111111; padding: 45px; border-radius: 5px;
        border-left: 15px solid #000000; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 21px; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 V17.0 The Final Kill (Zero-AI Signature)")
st.caption("Strategy: Dynamic Rhythm | Sensory Grit | No Robot Words")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original AI Text Dalein:", height=200)

# 4. The "Executioner" Prompt
executioner_prompt = """You are a professional human novelist. 
Your goal: Rewrite the text so it is 100% undetectable by AI sensors, while keeping it interesting for readers.

COMMANDS:
1. THE 1-3-1 FLOW: Start with a punchy 1-word sentence. Follow with 2-3 medium sentences. End the thought with a 1-word sentence. 
2. NO POETRY: Ban words like 'Symphony', 'Dance', 'Echo', 'Tapestry', 'Mournful', 'Melody'. Use 'Loud', 'Stink', 'Hard', 'Cold'.
3. PHYSICAL STRESS: Describe the character's body. Stinging sweat, dry throat, shaking hands, stomach acid. 
4. NO HEADINGS: Do not use 'Fear', 'Pain', or 'Rot' as headings. Mix them into the paragraph.
5. VARY SENTENCE LENGTH: Mix 3-word sentences with 20-word sentences. This breaks AI math.
6. HUMAN IMPERFECTION: Use 'I mean', 'Maybe', 'Actually', or em-dashes (—) to show a human mind thinking."""

if st.button("🚀 Execute Humanization"):
    if user_text:
        with st.spinner('Killing AI signature...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": executioner_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.5, 
                    top_p=0.7
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Professional Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Kuch likho bhai!")

st.markdown("---")
st.caption("Custom Built for Abubakar | V17.0 Stealth Mode")
