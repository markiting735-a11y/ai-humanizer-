import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="Abubakar's Gutter Stealth V16", page_icon="☢️", layout="wide")

# CSS: Raw & Edgy Interface
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; color: #ffffff !important; background-color: #000000 !important; border: 2px solid #ff0000; }
    .result-box {
        background-color: #fdfdfd; color: #000000; padding: 45px; border-radius: 0px;
        border-left: 20px solid #ff0000; font-family: 'Arial', sans-serif; white-space: pre-wrap;
        line-height: 1.6; font-size: 22px; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☢️ Gutter Stealth V16.0 (The Nuclear Option)")
st.caption("Strategy: Zero Poetry | Ugly Realism | Broken Math")

# 2. API Key
client = Groq(api_key="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")

# 3. Input
user_text = st.text_area("Paste AI Garbage Here:", height=200)

# 4. The "Anti-Poet" Master Prompt
# Is bar humne AI ko bad-tameez novelist banaya hai.
gutter_prompt = """You are a gritty, raw horror writer. 
Your goal: Rewrite this text to pass a 0% AI score. 

RULES OF DESTRUCTION:
1. BAN ALL BEAUTY: Delete words like 'serenade', 'melody', 'miasma', 'crystalline', 'recoil', 'fragile'. These are AI death-words. Use 'Stink', 'Noise', 'Rot', 'Cold', 'Hard'.
2. STOP THE REPETITION: If you mentioned 'heart' once, don't mention it again for 5 sentences. 
3. THE 5-WORD LIMIT: Every third sentence MUST be under 5 words.
4. UGLY SENSATIONS: Describe the sour taste of vomit in the throat, the wet sound of a shoe on rot, or the stinging itch of a bug bite. 
5. NO HEADINGS: Do not use words like 'Fear', 'Frostbite', or 'Blood' as headings. Just tell the story.
6. NO TRANSITIONS: Don't use 'As', 'When', 'While'. Just give the action. 
   - Example: 'He walked. The floor broke. He fell.'"""

if st.button("☢️ Nuke the AI Pattern"):
    if user_text:
        with st.spinner('Stripping the AI soul...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": gutter_prompt}, {"role": "user", "content": user_text}],
                    temperature=1.6, # Max chaos
                    top_p=0.6 # Focus on raw words
                )
                result = response.choices[0].message.content
                
                st.subheader("📖 Raw Manuscript:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result, language=None)
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kachra dalo!")

st.markdown("---")
st.caption("V16.0 Optimized | Designed for Abubakar to win the KDP War.")
