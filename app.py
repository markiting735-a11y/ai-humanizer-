import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Abubakar's AI Studio", page_icon="🚀", layout="centered")

# CSS Fix: unsafe_allow_html use karna tha
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    stTextArea textarea { font-size: 16px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Abubakar's Multi-Mood Humanizer")
st.markdown("Is tool se aap AI text ko 0% detection level par la sakte hain.")
st.markdown("---")

# 2. API Key Setup
client = Groq(api_key="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")

# 3. Sidebar for Settings
with st.sidebar:
    st.header("⚙️ Control Panel")
    mood = st.selectbox("Writing Style:", 
                        ["Super Human (Casual/Story)", "Professional (Book/Thriller)"])
    
    st.divider()
    st.write("**Tips for 0% AI Score:**")
    st.caption("1. Casual mode doston wali chat ke liye hai.")
    st.caption("2. Professional mode novels aur books ke liye hai.")

# 4. Input Area
user_text = st.text_area("Original AI Text Yahan Paste Karein:", height=250, placeholder="Once upon a time...")

# 5. Logic for Prompts
if mood == "Super Human (Casual/Story)":
    system_prompt = "You are a casual human writer. Use slang, messy grammar, and a conversational tone (omg, i mean, anyway). Use run-on sentences. Break all AI patterns to get 0% detection."
    temp = 1.4
else:
    system_prompt = "You are a world-class fiction author. Rewrite the text to be gripping and natural. Use descriptive human language and varied sentence lengths. Maintain proper grammar but avoid robotic AI structures."
    temp = 0.8

# 6. Execution Button
if st.button("✨ Humanize & Generate"):
    if user_text:
        with st.spinner('Converting... Please wait.'):
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
                
                # Output Section
                st.subheader("✅ Humanized Result:")
                
                # Built-in Copy Button via st.code
                st.code(result, language=None)
                
                # Word Counter logic
                word_count = len(result.split())
                st.info(f"📊 Word Count: {word_count} words")
                
                st.success("Upar diye gaye box ke top-right se copy kar lein! 📋")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch text to likhein!")

st.markdown("---")
st.caption("Developed with 🔥 by Abubakar | Class 11 CS Student")
