import streamlit as st
from groq import Groq

# 1. Page Configuration (Wide layout taake poora page use ho)
st.set_page_config(page_title="Abubakar's AI Studio", page_icon="🚀", layout="wide")

# CSS for better UI on Mobile
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; }
    .stCodeBlock { border: 2px solid #4CAF50 !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")
st.markdown("---")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Tone Selection (Ab ye Main Screen par hai)
st.subheader("⚙️ Settings")
mood = st.selectbox("Style Select Karein (Tone):", 
                    ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])

st.markdown("---")

# 4. Input Area
user_text = st.text_area("Original AI Text Yahan Paste Karein:", height=200, placeholder="Apni story yahan likhein...")

# 5. Logic for Prompts
if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a casual human writer. Use slang, messy grammar, and a conversational tone (omg, i mean, anyway). Break all AI patterns."
    temp = 1.4
else:
    system_prompt = "You are a professional novelist. Use engaging, high-quality human language with proper grammar. Avoid all robotic structures."
    temp = 0.8

# 6. Execution Button
if st.button("✨ Humanize & Generate"):
    if user_text:
        with st.spinner('Converting...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_text}
                    ],
                    temperature=temp
                )
                
                result = response.choices[0].message.content
                
                # Output Section (Pora page width use karega)
                st.subheader("✅ Humanized Result:")
                
                # st.code built-in copy button ke sath
                st.code(result, language=None)
                
                # Word Counter
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} words")
                
                st.success("Upar diye gaye box ke kone se copy kar lein! 📋")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch text to likhein!")

st.markdown("---")
st.caption("Developed by Abubakar | 0% AI Detection Mode")
