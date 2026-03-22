import streamlit as st
import numpy as np
from PIL import Image
import random

st.set_page_config(page_title="Leukemia Detection", layout="centered")

st.title("🧬 Leukemia Detection System (Demo)")

st.write("Upload a blood sample image to detect leukemia probability")

uploaded_file = st.file_uploader("Upload Blood Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        
        # 🔥 FAKE LOGIC (DEMO)
        leukemia = random.uniform(70, 95)
        healthy = 100 - leukemia

        # UI Output
        st.success(f"🧬 Leukemia Probability: {leukemia:.2f}%")
        st.success(f"💚 Healthy Probability: {healthy:.2f}%")

        # Risk Level
        st.subheader("Risk Level")

        if leukemia > 85:
            st.error("🔴 High Risk - Immediate medical attention required")
        elif leukemia > 70:
            st.warning("🟡 Moderate Risk - Further analysis recommended")
        else:
            st.success("🟢 Low Risk")

        # Progress bar
        st.progress(int(leukemia))
