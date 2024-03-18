import streamlit as st
import ollama

st.title("S4205066 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can i help?"}]

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message(message["role"], avatar="😀").write(message["content"])
    else:
        st.chat_message(message["role"], avatar="💬").write(message["content"])

def generate_response():
    response = ollama.chat(model="talisman825/unichatbot", stream=True, messages=st.session_state.messages)
    for partialResponse in response:
        token = partialResponse["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="😀").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="💬").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})