import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Ghost Protocol V15", page_icon="👻", layout="wide")

# CSS: Ghost Writer Style
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; color: #f0f0f0 !important; background-color: #0d1117 !important; border: 1px solid #30363d; }
    .result-box {
        background-color: #ffffff; color: #1a1a1a; padding: 45px; border-radius: 3px;
        border-right: 15px solid #1a1a1a; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.8; font-size: 21px; box-shadow: 10px 10px 40px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👻 Ghost Protocol V15.0 (No-Repeat Engine)")
st.caption("Strategy: Zero-Repetition | High Jitter | Gory Realism")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Original AI Content (Paste here):", height=200)

# 4. The "Anti-Pattern" Master Prompt
# Is bar instructions aur bhi sakht hain.
protocol_prompt = """You are a master novelist writing a horror scene. 
Rewrite the user text to be 100% human-unique.

STRICT ANTI-DETECTION RULES:
1. NO REPETITION: Do not use the same phrase twice. If you said 'heart was racing', next time use 'ribs were shaking' or 'pulse was thudding'. 
2. KILL THE CLICHES: Ban 'mind screaming', 'legs rooted to the spot', 'inexorable', 'oppressive'. Use raw, ugly descriptions.
3. VARY THE START: Don't start every paragraph with a single word like 'Fear' or 'Pain'. Mix it up.
4. JAGGED RHYTHM: One sentence must be a single word. The next must be a long, rambling thought. The next must be 5 words. Break the AI's math.
5. SENSORY VOMIT: Focus on the sour taste of stomach acid, the grit under the fingernails, or the smell of wet dog and iron.
6. NO ADVERBS: Remove 'slowly', 'frantically', 'eerily'. Show the panic through action."""

if st.button("💀 Execute Ghost Protocol"):
    if user_text:
        with st.spinner('Scrubbing AI patterns...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": protocol_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.5, # Max randomness to avoid repetition
                    top_p=0.75
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Clean Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Bhai, pehle text dalo!")

st.markdown("---")
st.caption("Developed for Abubakar | V15.0 Optimized for KDP Best-Sellers")
