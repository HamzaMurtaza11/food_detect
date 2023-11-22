import streamlit as st
import requests
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/dima806/food_type_image_detection_new"
headers = {"Authorization": "Bearer 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"}

def query(image_content):
    response = requests.post(API_URL, headers=headers, data=image_content)
    return response.json()

def main():
    st.title("Bawdic FoodVisiOn")
    st.sidebar.title("Upload Image")
    
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.sidebar.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.sidebar.write("")
        st.sidebar.write("Detect the food")

        # Make API call
        if st.sidebar.button("Detect"):
            image_content = uploaded_file.read()
            output = query(image_content)

            st.write("## Results")
            st.write(output)  # Display the API response

if __name__ == "__main__":
    main()
