import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ['OPENAI_API_KEY'] = openai_key

st.title('LangChain Demo with OpenAI API')
input_text= st.text_input("Search topic of interest")