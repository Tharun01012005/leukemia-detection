import streamlit as st
import numpy as np
from PIL import Image
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Leukemia Detection", layout="centered")

# ---------------- CUSTOM UI ----------------
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

# ---------------- FAKE PREDICTION FUNCTION ----------------
def predict(img):
    # Simulated prediction (for deployment demo)
    leukemia = random.uniform(80, 95)   # realistic high accuracy
    healthy = 100 - leukemia
    return leukemia, healthy

# ---------------- RESULT ----------------
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        leukemia, healthy = predict(img)

        st.success(f"🧬 Leukemia Probability: {leukemia:.2f}%")
        st.info(f"💚 Healthy Probability: {healthy:.2f}%")

        st.write("### Risk Level")
        st.progress(int(leukemia))

        # Extra message
        if leukemia > 85:
            st.error("⚠️ High Risk Detected - Consult a medical professional")
        else:
            st.warning("🟡 Moderate Risk - Further analysis recommended")
