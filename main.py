from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


st.title("AI Sensing")
input_text = st.text_input("Search the topic you want")

#Ollama
llm=Ollama(model="gpt-3.5-turbo")
