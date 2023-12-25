from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
logo_path = "logo.png" 


# function to load Gemini Pro modal and get responses

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
   # if input!="":
       # response=model.generate_content([input,image])
   #else:
    response=model.generate_content([input_blank,image])
    return response.text

## Initialize Streamlit app


st.set_page_config(page_title="Ask CloudBundle Image")
# Add a logo

st.image(logo_path, use_column_width=True)


st.header("Ask Gemini : ")

uploaded_file = st.file_uploader("Choose an image: ", type=["jpg","jpeg","png"])
image=""


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input_blank ="Describe this image in all aspects. including people, their age, face, social status, how they are looking, their emotions in picture, activity, objects, places in an article"
#input=st.text_input("Ask about this image : ", key="input")

submit=st.button("Tell me about this picture")

# If submit is clicked
if submit:

    response=get_gemini_response(input,image)
    st.subheader("Here you go...")
    st.write(response)