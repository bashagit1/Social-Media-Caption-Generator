import streamlit as st
import openai
import os
from SimplerLLM.language.llm import LLM, LLMProvider

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM instance
llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-3.5-turbo")

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
        response = llm_instance.generate_response(prompt=prompt)
        
        st.subheader("📝 Generated Caption")
        st.write(response)
        
        # Add Copy/Download Button for convenience
        st.download_button(label="⬇️ Download Caption", data=response, file_name="caption.txt")
    else:
        st.warning("⚠️ Please enter a theme or topic to generate a caption.")

# Display User Instructions
st.info("""
### How to Use:
1. Enter a theme or topic for your caption.
2. Select the social media platform and tone.
3. Click 'Generate Caption' to create your engaging content!
""")
