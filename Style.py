import streamlit as st
import google.generativeai as genai
from PIL import Image

# This version is the most stable for the 401 error
if "GOOGLE_API_KEY" in st.secrets:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
else:
    st.error("Please add your GOOGLE_API_KEY to the Streamlit Secrets.")

st.set_page_config(page_title="AI Persona Stylist", layout="wide")

st.title("👗 AI Persona & Style Consultant")

uploaded_file = st.file_uploader("Upload a clear photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, width=300)
    
    if st.button("Generate My Style Blueprint"):
        with st.spinner("Analyzing your style..."):
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            prompt = """
            Analyze this photo for:
            1. Body Shape & Facial Essence
            2. Best Color Palette & Texture
            3. Recommended Clothing Silhouettes
            4. 3 Outfit Formulas (Work, Casual, Evening)
            """
            
            try:
                response = model.generate_content([prompt, image])
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
