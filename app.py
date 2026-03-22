def predict(img_file):
    try:
        files = {
            "file": ("image.jpg", img_file.getvalue(), "image/jpeg")
        }

        headers = {
            "ngrok-skip-browser-warning": "true"
        }

        response = requests.post(API_URL, files=files, headers=headers)

        st.write("Status:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            data = response.json()
            return data["leukemia"], data["healthy"]
        else:
            st.error("❌ API Error. Check response above.")
            return None, None

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        return None, None
