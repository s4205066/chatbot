import streamlit as st
from langchain_openai import OpenAI
import time

st.title("Langchain Chatbot")

api_key = st.sidebar.text_input('OpenAI API Key', type='password')

llm = OpenAI(openai_api_key = api_key)

def response_generator(message):
    response = llm.invoke(message)

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

with st.chat_message("assistant"):
    st.write_stream("I'm an AI Assistant. How can i help?")

if "langchain_messages" not in st.session_state:
    st.session_state.langchain_messages = []

for message in st.session_state.langchain_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter Message:"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.langchain_messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    st.session_state.langchain_messages.append({"role": "assistant", "content": response})






