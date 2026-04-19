import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's AI Studio", page_icon="🚀", layout="wide")

# CSS: Mobile par text ko wrap karne ke liye
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 16px !important; color: #ffffff !important; background-color: #262730 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Writing Studio")
st.markdown("---")

client = Groq(api_key="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")

st.subheader("⚙️ Settings")
mood = st.selectbox("Style Select Karein (Tone):", ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])

st.markdown("---")

user_text = st.text_area("Original AI Text Yahan Paste Karein:", height=200)

if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a casual human writer. Use slang, messy grammar, and conversational tone. Break all AI patterns."
    temp = 1.4
else:
    system_prompt = "You are a professional novelist. Use high-quality human language. Avoid robotic structures."
    temp = 0.8

if st.button("✨ Humanize & Generate"):
    if user_text:
        with st.spinner('Converting...'):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_text}],
                    temperature=temp
                )
                
                result = response.choices[0].message.content
                
                st.subheader("✅ Humanized Result:")
                
                # FIX: st.code ki jagah text_area jo neechay line wrap karega
                st.text_area("Result (Copy selection se karein):", value=result, height=300, key="output_text")
                
                # Word Counter
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} words")
                
                st.success("Mobile par text par long-press kar ke copy kar lein! 📋")
                
            except Exception as e:
                st.error(f"Error: {e}")
                
