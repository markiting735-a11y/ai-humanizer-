import streamlit as st
from groq import Groq
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Author Studio", page_icon="✍️", layout="wide")

# CSS: Professional Author Theme
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1a1a1a !important; }
    .result-box {
        background-color: #fdfdfd; color: #1a1a1a; padding: 30px; border-radius: 8px;
        border-left: 10px solid #2e7d32; font-family: 'Georgia', serif; white-space: pre-wrap;
        margin-top: 15px; line-height: 1.8; font-size: 19px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 Abubakar's Author Studio (V6.0 - KDP Edition)")
st.caption("Target: KDP Professional Quality | Mode: Deep Human Perspective")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Input Area
user_text = st.text_area("AI Text Yahan Paste Karein:", height=250, placeholder="Write your story draft here...")

# 4. The "Professional Novelist" Prompt (Balanced for Books)
# Ye prompt AI ko professional author banata hai jo human touch ke sath likhta hai
author_stealth_prompt = """You are a world-class thriller novelist. 
Rewrite the user's text to pass AI detection while maintaining high-quality professional literature standards for a book.

STRICT INSTRUCTIONS:
1. DEEP POINT OF VIEW: Describe what the character feels, smells, and hears. (e.g., instead of 'he was scared', use 'the hair on his neck stood up').
2. VARY SENTENCE STRUCTURE: Mix short, punchy sentences with longer, flowing descriptions. This destroys AI's rhythmic pattern.
3. NO REPETITION: Use synonyms. Never repeat the same key noun more than twice in a paragraph.
4. HUMAN PACING: Use dashes (—) for sudden interruptions and ellipses (...) for trailing thoughts, but keep it professional.
5. BAN AI SIGNATURES: No 'shrouded', 'testament', 'vibrant', 'delve', or 'interplay'. Use raw, strong English verbs.
6. REAL DIALOGUE: If there is thought or speech, make it sound like a real person, not a robot.
7. NO HEADINGS: Just pure, clean, book-ready paragraphs."""

if st.button("📖 Generate Book-Ready Chapter"):
    if user_text:
        with st.spinner('Crafting your masterpiece...'):
            try:
                # Optimized parameters for high-quality storytelling
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": author_stealth_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=1.1, # Slightly high for creativity
                    top_p=0.9
                )
                
                result = response.choices[0].message.content
                
                # Output Section
                st.subheader("🖋️ Professional Book Content:")
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                
                st.write("📋 **Final Text for KDP:**")
                st.code(result, language=None)
                
                st.success("Quality Checked. Patterns Broken. Ready for Publishing.")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Bhai, draft toh paste karo!")

st.markdown("---")
st.caption("Optimized for Amazon KDP & Draft2Digital | Created by Abubakar")

