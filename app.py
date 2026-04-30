import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Ghost-Writer Elite", page_icon="🕵️", layout="wide")

# CSS: Dark Premium Interface
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 17px !important; color: #e0e0e0 !important; background-color: #121212 !important; border: 1px solid #444; }
    .result-box {
        background-color: #ffffff; color: #1a1a1a; padding: 40px; border-radius: 2px;
        border-left: 12px solid #1a1a1a; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.9; font-size: 20px; box-shadow: 15px 15px 0px #eeeeee;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️ Ghost-Writer Elite (V11.1)")
st.caption("Status: Undetectable | Style: Professional Thriller | Model: Llama 3.3 70B")

# 2. API Key
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("Original Story Draft (Raw Content):", height=200, placeholder="Enter your story beats here...")

# 4. The "Anti-AI" Master Prompt
master_prompt = """You are a world-class ghostwriter. Rewrite the input text to pass 100% human detection. 

STRICT GUIDELINES TO KILL AI DETECTION:
1. KILL THE FLOW: Use fragments. Short bursts of action. (e.g., 'Cold. Dark. Then, a scream.')
2. SENSORY VOMIT: Focus on physical panic. (Sweat, metallic taste, ringing ears, chest pain).
3. NO 'AI' WORDS: Ban words like 'enveloped', 'shrouded', 'reverberated', 'palpable', 'testament'. Use 'Heavy', 'Loud', 'Felt like'.
4. EXTREME BURSTINESS: Follow a 40-word sentence with a 1-word sentence. 
5. NO CONNECTORS: Remove 'However', 'Therefore', 'Suddenly'. 
6. THE 'HUMAN GLITCH': Use em-dashes (—) and ellipses (...) to show thinking gaps."""

if st.button("🚀 Transform to Human Masterpiece"):
    if user_text:
        with st.spinner('Stripping AI Signatures...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": master_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.25, 
                    top_p=0.85
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Final Human-Grade Manuscript:")
                # FIXED: Change unsafe_allow_True to unsafe_allow_html
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Raw Text for KDP:**")
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch likho toh sahi!")

st.markdown("---")
st.caption("Built for Abubakar | Optimized for Zero-AI Detection.")
