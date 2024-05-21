import requests
import streamlit as st

def openai_response(input_text):
    response = requests.post("http://localhost:8000/instructions/invoke",
                             json={"input":{"topic":input_text}})
    return response.json()['output']['content']

def ollama_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input":{"topic":input_text}})
    return response.json()['output']

st.title("Complete-LangChain-App")
input_text = st.text_input("Write instructions on")
input_text1 = st.text_input("Write essay on")

if input_text:
    st.write(openai_response(input_text))

if input_text1:
    st.write(ollama_response(input_text1))