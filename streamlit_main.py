import streamlit as st
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from openai import OpenAI

# https://discuss.streamlit.io/t/adding-a-long-pdf-as-a-custom-data-source/57348
# https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/


st.header("S4205066 Chatbot")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question!"}
    ]

OpenAI.api_key = st.secrets.openai_key

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading data."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the University of Gloucestershire and your job is to answer questions. Assume that all questions are related to the University of Gloucestershire. Keep your answers professional and based on facts – do not hallucinate features."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index
    
index = load_data()

chat_engine = index.as_chat_engine(chat_mode="condese_question", verbose=True)

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message= {"role": "assistant", "content": response}
            st.session_state.messages.append(message)