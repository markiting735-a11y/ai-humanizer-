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

# Tabs for separate functions
tab1, tab2 = st.tabs(["🚀 Auto-KDP Ebook Agent", "🤖 Single Text Humanizer"])

# --- TAB 1: FULL AUTOMATION (Your Requirement) ---
with tab1:
    st.header("📚 Full Ebook Automation")
    st.caption("Topic dalo, system khud chapters likhega, humanize karega aur Word file dega.")
    
    col1, col2 = st.columns(2)
    with col1:
        book_topic = st.text_input("Ebook Topic:", placeholder="e.g. 3D Modeling Masterclass")
    with col2:
        book_lang = st.selectbox("Language:", ["English", "Urdu", "Roman Urdu"])
    
    num_chapters = st.slider("Kitne Chapters chahiye?", 1, 10, 3)

    if st.button("Generate & Humanize Full Ebook"):
        if book_topic:
            doc = Document()
            
            # Title Page
            title = doc.add_heading(book_topic, 0)
            title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_page_break()
            
            # Copyright Page
            doc.add_heading('Copyright & Disclaimer', level=1)
            doc.add_paragraph(f"This book was generated and humanized by Abubakar's AI Studio.\n© 2026 All Rights Reserved.\nLanguage: {book_lang}")
            doc.add_page_break()

            progress_bar = st.progress(0)
            
            for i in range(1, num_chapters + 1):
                st.write(f"✍️ Writing Chapter {i}...")
                
                # A. Generate Content
                raw_res = client.chat.completions.create(
                    model="llama-3.1-70b-versatile",
                    messages=[{"role": "user", "content": f"Write a detailed Chapter {i} for a book titled '{book_topic}' in {book_lang}. Focus on depth and quality."}]
                ).choices[0].message.content
                
                # B. Humanize Content (Using your EXACT Novelist Logic)
                human_res = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a rebellious, emotional human novelist. Rewrite text so it's 100% IMPOSSIBLE to detect as AI. Use jagged rhythm, sensory overload, and fragments. NO AI WORDS like 'delve' or 'labyrinth'."},
                        {"role": "user", "content": raw_res}
                    ],
                    temperature=1.45
                ).choices[0].message.content
                
                # C. Add to Docx
                doc.add_heading(f"Chapter {i}", level=1)
                doc.add_paragraph(human_res)
                doc.add_page_break()
                
                progress_bar.progress(i / num_chapters)

            # Save and Download
            buffer = io.BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            
            st.success("✅ Pori File Ready He! Ek word ki formatting ghalti nahi hogi.")
            st.download_button(
                label="📥 Download KDP Ready Ebook (.docx)",
                data=buffer,
                file_name=f"{book_topic}_Humanized.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        else:
            st.warning("Pehle topic toh likho!")

# --- TAB 2: ORIGINAL HUMANIZER (No Changes) ---
with tab2:
    st.header("🤖 Abubakar's Writing Studio")
    st.caption("ULTRA-STEALTH MODE: Single Paragraph Testing")
    
    mood = st.selectbox("Style Select Karein:", ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])
    user_text = st.text_area("AI Text Yahan Paste Karein:", height=250)

    if st.button("✨ Humanize & Destroy AI Patterns"):
        if user_text:
            random_factor = random.uniform(0.05, 0.25)
            if mood == "Super Human (Casual/Story)":
                sys_prompt = "You are a messy human storyteller. Use slang, 'uhm', 'like', 'literally', and occasional typos."
                temp = 1.4 + random_factor
            else:
                sys_prompt = "You are a rebellious, emotional human novelist. Rewrite the text so it's 100% IMPOSSIBLE to detect as AI. Sound raw, tired, and real."
                temp = 1.35 + random_factor

            with st.spinner('Processing...'):
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_text}],
                    temperature=temp
                )
                result = response.choices[0].message.content
                st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)
                st.code(result)
            
