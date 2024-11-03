import streamlit as st
import os
from openai import OpenAI

# Set up OpenAI API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title and Description
st.set_page_config(page_title="Social Media Caption Generator", page_icon="✍️")

# Title and Description with Character Icons
st.markdown("<h1 style='text-align: center;'>✨ Social Media Caption Generator ✨</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Generate engaging captions for your social media posts.</h4>", unsafe_allow_html=True)

# Sidebar for input options with icons
with st.sidebar:
    st.header("🤖 Options")
    platform = st.selectbox("📱 Select Social Media Platform", ["Instagram", "Facebook", "Twitter", "LinkedIn"])
    tone = st.selectbox("🎤 Select Tone", ["Fun", "Serious", "Inspirational", "Motivational", "Witty"])

# User Input for topic/theme
user_input = st.text_input("💬 Enter the theme or topic for your caption", placeholder="e.g., Traveling in Paris")

# Generate and Display Response
if st.button("🚀 Generate Caption", key="generate"):
    if user_input:
        prompt = f"Generate a {tone.lower()} caption for a {platform.lower()} post about {user_input}."
        
        # Generate response from LLM
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo"
        )
        
        caption = response.choices[0].message.content
        
        st.subheader("📝 Generated Caption")
        st.write(caption)
        
        # Add Copy/Download Button for convenience
        st.download_button(label="⬇️ Download Caption", data=caption, file_name="caption.txt")
    else:
        st.warning("⚠️ Please enter a theme or topic to generate a caption.")

# Display User Instructions
st.info("""
### How to Use:
1. Enter a theme or topic for your caption.
2. Select the social media platform and tone.
3. Click 'Generate Caption' to create your engaging content!
""")
