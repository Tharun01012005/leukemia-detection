import streamlit as st
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

# Load TFLite model
interpreter = tflite.Interpreter(model_path="leukemia_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

IMG_SIZE = 224

st.set_page_config(page_title="Leukemia Detection", layout="centered")
st.title("🧬 Leukemia Detection System")

uploaded_file = st.file_uploader("Upload Blood Image", type=["jpg","png","jpeg"])

def predict(img):
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    pred = interpreter.get_tensor(output_details[0]['index'])[0][0]

    leukemia = pred * 100
    healthy = (1 - pred) * 100

    return leukemia, healthy

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)

    if st.button("Analyze"):
        leukemia, healthy = predict(img)

        st.success(f"Leukemia: {leukemia:.2f}%")
        st.info(f"Healthy: {healthy:.2f}%")
        st.progress(int(leukemia))
