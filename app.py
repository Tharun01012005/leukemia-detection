import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
model = load_model("leukemia_squeezenet_fast.h5")

IMG_SIZE = 224

# UI
st.set_page_config(page_title="Leukemia Detection", layout="centered")

st.title("🧬 Leukemia Detection System")
st.write("Upload a blood sample image to detect leukemia probability")

uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg","png","jpeg"])

def predict(img):
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]

    leukemia = pred * 100
    healthy = (1 - pred) * 100

    return leukemia, healthy

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

    if st.button("🔍 Analyze"):
        leukemia, healthy = predict(img)

        st.success(f"🧬 Leukemia Probability: {leukemia:.2f}%")
        st.info(f"💚 Healthy Probability: {healthy:.2f}%")
        st.progress(int(leukemia))