import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. SETUP: Your API Key is now integrated
API_KEY = "AQ.Ab8RN6IWJL1yDpGGvLCXXgIVO3BrdoFmNwDECHUNlMdtgAGlxQ"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="AI Persona Stylist", layout="wide")

# Custom Styling for a "Luxury" look
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1E1E1E;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👗 AI Persona & Style Consultant")
st.write("Upload a clear photo to analyze your body shape, skin tone, and 'outer personality'.")

# 2. THE UI: Image Upload
uploaded_file = st.file_uploader("Upload a clear full-body or portrait photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)
    
    with col2:
        if st.button("Generate My Style Blueprint"):
            with st.spinner("Analyzing your unique geometry and essence..."):
                # 3. THE BRAIN: The Instructions
                model = genai.GenerativeModel('gemini-2.0-flash')
                
                prompt = """
                You are a world-class fashion consultant and image architect. 
                Analyze this photo and provide a detailed 'Style Identity' report:

                1. PHYSICAL GEOMETRY: Identify body shape (e.g., hourglass, rectangle, etc.) and facial bone structure.
                2. COLOR ANALYTICS: Determine skin undertone (cool/warm) and the 'Seasonal Color Palette'.
                3. OUTER PERSONALITY: Based on their physical presence, what archetype do they project? (e.g., The Ruler, The Sage, The Romantic).
                4. FABRIC & TEXTURE: Recommend specific materials (e.g., crisp linen, heavy silk, structured wool) that suit their frame.
                5. THE STYLE FORMULA: 
                   - Recommended Silhouettes (e.g., high-waisted, sharp shoulders).
                   - Colors to avoid vs. colors to embrace.
                   - Three outfit 'Blueprints' (Professional, Casual, and Statement/Evening).
                
                Keep it sophisticated, actionable, and encouraging.
                """

                try:
                    response = model.generate_content([prompt, image])
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

# Sidebar Guide
with st.sidebar:
    st.header("How to get best results")
    st.write("1. Use natural daylight.")
    st.write("2. Stand against a plain wall.")
    st.write("3. Ensure your full body/face is visible.")
  
