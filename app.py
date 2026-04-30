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

st.title("🕵️ Ghost-Writer Elite (V11.0)")
st.caption("Status: Undetectable | Style: High-Stakes Thriller | Focus: Reader Engagement")

# 2. API Key
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("Original Story Draft (Raw Content):", height=200, placeholder="Enter your story beats here...")

# 4. The "Anti-AI" Master Prompt
# Is prompt mein humne AI ko 'Author' nahi 'Observer' banaya hai.
master_prompt = """You are a world-class ghostwriter. Rewrite the input text to pass 100% human detection. 

STRICT GUIDELINES TO KILL AI DETECTION:
1. KILL THE FLOW: AI is too smooth. You must be jagged. Use fragments. (e.g., 'Dead silence. Then, a creak.')
2. SENSORY VOMIT: Instead of describing the room, describe the character's physical panic. (Sweat, itching, metallic taste, ringing ears).
3. NO 'PURITY': Avoid words like 'enveloped', 'shrouded', 'reverberated', 'palpable', 'testament'. These are AI death-sentences. Use 'Heavy', 'Loud', 'Felt like'.
4. VARY SENTENCE LENGTH (EXTREME): Follow a 30-word sentence with a 2-word sentence. This destroys AI probability math.
5. NO CONNECTORS: Remove 'However', 'Therefore', 'Suddenly', 'Moreover'. Start sentences abruptly. 
6. ACTIVE VOICE ONLY: Don't say 'The door was opened'. Say 'He kicked the door open.'
7. THE 'HUMAN TOUCH': Use em-dashes (—) and ellipses (...) to show a mind that is thinking, not a machine that is calculating."""

if st.button("🚀 Transform to Human Masterpiece"):
    if user_text:
        with st.spinner('Stripping AI Signatures...'):
            try:
                # Using the latest high-capacity model
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": master_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.25, # High randomness to break patterns
                    top_p=0.85
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Final Human-Grade Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_True=True)
                
                st.write("📋 **Raw Text for KDP Copying:**")
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch likho toh sahi!")

st.markdown("---")
st.caption("Built for Abubakar | Optimized for Zero-AI Detection and High Reader Retention.")
