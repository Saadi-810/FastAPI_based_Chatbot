import streamlit as st
import requests
import os 
# Backend API URL
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000/chat")

st.set_page_config(page_title="LLM Chatbot", page_icon="🤖")

st.title("🤖 LLM Chatbot")
st.write("Ask anything. Powered by Groq LLM.")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend API
    response = requests.post(
        BACKEND_URL,
        json={"message": user_input}
    )

    if response.status_code == 200:
        reply = response.json()["reply"]
    else:
        reply = "⚠️ Error communicating with backend."

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)
