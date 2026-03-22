import streamlit as st
import numpy as np
from PIL import Image
import requests

# 🔥 YOUR REAL API URL (already working)
API_URL = "https://cosmogonic-untactically-kevin.ngrok-free.dev/predict"

IMG_SIZE = 224

# ---------------- UI SETTINGS ----------------
st.set_page_config(page_title="Leukemia Detection", layout="centered")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🧬 Leukemia Detection System")
st.write("Upload a blood sample image to detect leukemia probability")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload Blood Image", type=["jpg", "png", "jpeg"])

# ---------------- PREDICTION FUNCTION ----------------
def predict(img_file):
    try:
        response = requests.post(API_URL, files={"file": img_file})

        if response.status_code == 200:
            data = response.json()
            return data["leukemia"], data["healthy"]
        else:
            st.error("❌ API Error. Please try again.")
            return None, None

    except:
        st.error("⚠️ Unable to connect to API. Make sure Colab is running.")
        return None, None

# ---------------- RESULT ----------------
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        leukemia, healthy = predict(uploaded_file)

        if leukemia is not None:
            st.success(f"🧬 Leukemia Probability: {leukemia:.2f}%")
            st.info(f"💚 Healthy Probability: {healthy:.2f}%")

            st.write("### Risk Level")
            st.progress(int(leukemia))

            if leukemia > 85:
                st.error("⚠️ High Risk Detected - Consult a doctor immediately")
            elif leukemia > 60:
                st.warning("🟡 Moderate Risk - Further medical analysis recommended")
            else:
                st.success("✅ Low Risk - Normal condition")
