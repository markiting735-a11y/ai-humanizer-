import streamlit as st
from groq import Groq
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
import random

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's Pro Studio", page_icon="✍️", layout="wide")

# API Key Setup
client = Groq(api_key="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")

st.title("🛡️ Professional Ebook Agent (Safe Mode)")
st.markdown("---")

# Tabs for Workflow
tab1, tab2, tab3 = st.tabs(["1️⃣ AI Content Writer", "2️⃣ Manual Humanizer", "3️⃣ Pro Formatter (ToC/Copyright)"])

# --- STEP 1: RAW WRITER (No Search/No Sources) ---
with tab1:
    st.subheader("Bina Citations ke Content Likhwayein")
    raw_topic = st.text_input("Chapter ka Topic ya Heading:")
    lang_opt = st.selectbox("Language:", ["English", "Urdu", "Roman Urdu"])
    
    if st.button("Generate Clean Content"):
        if raw_topic:
            with st.spinner("AI is thinking..."):
                # Strictly prohibiting search tags
                res = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a professional author. Write a detailed book chapter. DO NOT use internet search, DO NOT include citations, source tags, or numbers. Pure text only."},
                        {"role": "user", "content": f"Write a long chapter in {lang_opt} about: {raw_topic}"}
                    ],
                    temperature=0.8
                ).choices[0].message.content
                st.text_area("Raw Output (Isay Copy karein):", value=res, height=300)
                st.info("💡 Is text ko copy karke Step 2 mein paste karein.")

# --- STEP 2: HUMANIZER (Rebellious Novelist Mode) ---
with tab2:
    st.subheader("🤖 Humanizer: AI Patterns ko Khatam Karein")
    to_humanize = st.text_area("Raw Text Yahan Paste Karein:", height=300)
    
    if st.button("✨ Humanize (Novelist Style)"):
        if to_humanize:
            with st.spinner("Adding human soul to text..."):
                # Your specific high-temperature humanizer logic
                human_res = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a rebellious human novelist. Rewrite the text so it's 100% impossible to detect as AI. Use jagged rhythm, sensory overload, fragments, and raw emotion. Absolutely NO AI words like 'delve' or 'comprehensive'."},
                        {"role": "user", "content": to_humanize}
                    ],
                    temperature=1.45
                ).choices[0].message.content
                st.markdown("### ✅ Humanized Text (Format ke liye Copy karein):")
                st.write(human_res)
                st.code(human_res)

# --- STEP 3: PRO FORMATTER (KDP READY) ---
with tab3:
    st.subheader("📥 Final Book Formatting")
    
    col_t, col_a = st.columns(2)
    with col_t:
        book_title = st.text_input("Book Title:")
    with col_a:
        author_name = st.text_input("Author Name (Pen Name):")
    
    # Input area for multiple chapters
    final_text = st.text_area("Humanized Text Paste Karein (Chapters ke darmiyan 'CHAPTER_BREAK' likhein):", height=300)
    
    if st.button("Generate Professional .docx"):
        if final_text and book_title:
            doc = Document()
            
            # 1. TITLE PAGE
            title_p = doc.add_heading('\n\n\n' + book_title.upper(), 0)
            title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_paragraph(f"\n\n\nBy\n{author_name}").alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_page_break()
            
            # 2. COPYRIGHT PAGE
            doc.add_heading('Copyright', level=1)
            doc.add_paragraph(f"\n© 2026 {author_name}\nAll rights reserved. This book or any portion thereof may not be reproduced without express written permission.")
            doc.add_page_break()
            
            # 3. TABLE OF CONTENTS
            doc.add_heading('Table of Contents', level=1)
            chaps = final_text.split("CHAPTER_BREAK")
            for i in range(1, len(chaps) + 1):
                doc.add_paragraph(f"Chapter {i} ................................. Page {i+2}")
            doc.add_page_break()
            
            # 4. CONTENT INSERTION
            for i, content in enumerate(chaps, 1):
                doc.add_heading(f"Chapter {i}", level=1)
                doc.add_paragraph(content.strip())
                doc.add_page_break()
            
            # Save to memory
            buf = io.BytesIO()
            doc.save(buf)
            buf.seek(0)
            st.success("Professional Book Tayyar Hai!")
            st.download_button(f"📥 Download {book_title}.docx", buf, f"{book_title}.docx")
                
