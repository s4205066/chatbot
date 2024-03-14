import streamlit as st
import random
import time

st.title("Streaming Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter Message:"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.message.append({"role": "user", "content": prompt})

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )

    for word in response.split():
        yield word + " "
        time.sleep(0.05)
