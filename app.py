def predict(img_file):
    try:
        files = {
            "file": (img_file.name, img_file.getvalue(), img_file.type)
        }

        headers = {
            "ngrok-skip-browser-warning": "true"
        }

        response = requests.post(API_URL, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["leukemia"], data["healthy"]
        else:
            st.error("❌ API Error. Check logs.")
            return None, None

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
        return None, None
