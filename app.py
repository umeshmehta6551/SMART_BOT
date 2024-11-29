
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import google.generativeai as genai 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-flash-1,5")
model = genai.GenerativeModel("gemini-pro")
def my_output(query) ->str:
    response =model.generate_content(query)
    return response.text

### UI Development using Streamlit

st.set_page_config(page_title="SMART_BOT")
st.header("SMART_BOT")
input = st.text_input("Input" ,key = "input")
submit = st.button("ASk your  Query")

if submit:
    response=my_output(input)
    st.subheader("The Response is=")
    st.write(response)

    ## streamlit run app.py