import streamlit as st
import ollama

st.set_page_config(
    page_title="Free AI Chat Bot",
    page_icon="🤖"
)

st.title("🤖 Free Local AI Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

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

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_reply
    })
