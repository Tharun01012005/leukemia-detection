import streamlit as st
import requests
from PIL import Image

st.title("🧬 Leukemia Detection")

API_URL = "https://cosmogonic-untactically-kevin.ngrok-free.dev/predict"

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file)

    if st.button("Analyze"):
        try:
            files = {
                "file": ("image.jpg", uploaded_file.getvalue(), "image/jpeg")
            }

            headers = {
                "ngrok-skip-browser-warning": "true"
            }

            response = requests.post(API_URL, files=files, headers=headers)

            st.write("Status:", response.status_code)
            st.write("Response:", response.text)

            if response.status_code == 200:
                data = response.json()
                st.success(f"Leukemia: {data['leukemia']:.2f}%")
                st.success(f"Healthy: {data['healthy']:.2f}%")
            else:
                st.error("API Error")

        except Exception as e:
            st.error(f"Error: {e}")
