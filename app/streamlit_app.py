import streamlit as st
import os
import requests

API_URL = os.getenv('API_URL','http://localhost:8000/agent')
st.title("GenAI Agent Framework")
query = st.text_input("Enter your query:")
if st.button("Ask") and query:
    res = requests.get(API_URL, params={'q': query}).json()
    st.subheader("Thoughts")
    st.write(res.get('thoughts',''))
    st.subheader("Action")
    st.write(res.get('action',''))
    st.subheader("Result")
    st.write(res.get('result',''))
