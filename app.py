import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Rhythm Breaker", page_icon="⚡", layout="wide")

# CSS: Professional Midnight Theme
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 17px !important; color: #e0e0e0 !important; background-color: #1a1a1a !important; }
    .result-box {
        background-color: #ffffff; color: #111111; padding: 40px; border-radius: 4px;
        border-left: 10px solid #ff4b4b; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 20px; box-shadow: 10px 10px 30px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Rhythm Breaker V12.0 (The AI Killer)")
st.caption("Strategy: Variable Sentence Length + Sensory Overload")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original Content Yahan Dalein:", height=200)

# 4. The "Variable Rhythm" Prompt
rhythm_prompt = """You are a professional human novelist. Rewrite the user text to be 100% human-passing.

STRICT RHYTHM RULES:
1. THE 10-16-6 RULE: Constantly change sentence length. Write one long, descriptive sentence (20+ words), then a medium one (10-12 words), then a very short, punchy one (2-4 words). 
2. SENSORY DETAILS: Don't tell me he's scared. Tell me about the metallic taste of blood in his mouth or the way his shirt is sticking to his sweaty back.
3. WORDS TO BAN: Kill all AI favorites: 'Suddenly', 'However', 'Moreover', 'Enveloped', 'Shrouded', 'Testament', 'Coalesced'.
4. HUMAN DIALECT: Use words like 'Maybe', 'Actually', 'I mean', 'Sort of' to sound like a human thinking.
5. NO REPETITION: Use 'The beam' then 'The flickering light' then 'The yellow glow'. 
6. THE HOOK: Make the atmosphere heavy and professional, but keep the structure unpredictable."""

if st.button("🔥 Generate Undetectable Chapter"):
    if user_text:
        with st.spinner('Breaking the AI Pattern...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", 
                    messages=[{"role": "system", "content": rhythm_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.3, # Maximum unpredictability
                    top_p=0.9
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Professional Manuscript (0% AI Potential):")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle text toh dalo!")

st.markdown("---")
st.caption("Optimized for KDP | Strategy by Abubakar")
