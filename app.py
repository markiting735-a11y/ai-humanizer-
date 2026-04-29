import streamlit as st
from groq import Groq
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Auto-KDP Studio", page_icon="🚀", layout="wide")

# CSS for UI
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #1e1e1e !important; }
    .result-box {
        background-color: #0e1117; color: #e0e0e0; padding: 20px; border-radius: 12px;
        border: 2px solid #ff4b4b; font-family: 'Georgia', serif; white-space: pre-wrap;
        line-height: 1.7; margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. API Key Setup
client = Groq(api_key="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")

# Tabs
tab1, tab2 = st.tabs(["🚀 Auto-KDP Ebook Agent", "🤖 Single Text Humanizer"])

# --- TAB 1: FULL AUTOMATION ---
with tab1:
    st.header("📚 Full Ebook Automation")
    st.caption("Topic dalo, system khud chapters likhega aur Word file dega.")
    
    col1, col2 = st.columns(2)
    with col1:
        book_topic = st.text_input("Ebook Topic:", key="ebook_topic")
    with col2:
        book_lang = st.selectbox("Language:", ["English", "Urdu", "Roman Urdu"], key="ebook_lang")
    
    num_chapters = st.slider("Kitne Chapters?", 1, 5, 3) # Chapters thore kam rakhe hain for safety

    if st.button("Generate Full Ebook"):
        if book_topic:
            doc = Document()
            # Title Page
            title = doc.add_heading(book_topic, 0)
            title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_page_break()

            progress_bar = st.progress(0)
            
            for i in range(1, num_chapters + 1):
                st.write(f"✍️ Processing Chapter {i}...")
                
                try:
                    # Model change to 8b for stability (Free tier best model)
                    raw_res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[{"role": "user", "content": f"Write a detailed Chapter {i} for book '{book_topic}' in {book_lang}."}]
                    ).choices[0].message.content
                    
                    # Humanizing
                    human_res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {"role": "system", "content": "You are a rebellious human novelist. Rewrite text so it's 100% IMPOSSIBLE to detect as AI. Use jagged rhythm, sensory overload. NO AI WORDS like 'delve'."},
                            {"role": "user", "content": raw_res}
                        ],
                        temperature=1.4
                    ).choices[0].message.content
                    
                    doc.add_heading(f"Chapter {i}", level=1)
                    doc.add_paragraph(human_res)
                    doc.add_page_break()
                except Exception as e:
                    st.error(f"Quota error on Chapter {i}. Try again in 1 minute.")
                    break
                
                progress_bar.progress(i / num_chapters)

            buffer = io.BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            
            st.download_button(label="📥 Download File", data=buffer, file_name=f"{book_topic}.docx")

# --- TAB 2: ORIGINAL HUMANIZER ---
with tab2:
    st.header("🤖 Writing Studio")
    mood = st.selectbox("Style:", ["Super Human", "Professional"], key="mood_select")
    user_text = st.text_area("Paste AI Text:", height=200, key="human_input")

    if st.button("✨ Humanize Now"):
        if user_text:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "system", "content": "You are a human writer..."}, {"role": "user", "content": user_text}],
                temperature=1.4
            )
            st.markdown(f'<div class="result-box">{response.choices[0].message.content}</div>', unsafe_allow_html=True)
            
