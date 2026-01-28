import streamlit as st
import ollama

st.set_page_config(page_title="Free AI Chat Bot", page_icon="🤖")

st.title("🤖 Free Local AI Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="phi3",
                messages=st.session_state.messages
            )
            ai_reply = response["message"]["content"]
            st.write(ai_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )
