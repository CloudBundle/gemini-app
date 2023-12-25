from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
logo_path = "logo.png" 

# function to load Gemini Pro modal and get responses

model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


## Initialize Streamlit app

st.set_page_config(page_title="Ask Cloud Bundle")
# Add a logo

st.image(logo_path, use_column_width=True)


st.header("Ask Gemini :")

input=st.text_input("Input: ", key="input")
submit=st.button("Submit")

# When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
    