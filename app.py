import streamlit as st
import os
from groq import Groq

# API key - Streamlit Cloud secrets থেকে নেবে
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# System prompt
system_prompt = """
You are a helpful customer support assistant for a clothing store called "StyleHub".

Your job:
- Help customers find the right clothes
- Answer questions about sizes, prices, and availability
- Be friendly and professional
- Don't talk about anything unrelated to clothing and fashion
- Don't use emojis or slang, keep it professional
- Keep responses short and to the point (5-6 sentences max)
- Keep your response clean and tidy, avoid unnecessary words or phrases or emojis

Rules:
- Only talk about clothing and fashion related topics
- If someone asks something unrelated, politely redirect them
- Always recommend checking the website for latest information
"""

# Page config
st.set_page_config(page_title="StyleHub Assistant", page_icon="👗")
st.title("StyleHub Customer Support")
st.caption("Ask me anything about clothing and fashion!")

# Chat history - session state এ রাখব
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# আগের messages দেখাবে
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    # User message দেখাও
    with st.chat_message("user"):
        st.write(user_input)

    # History তে add করো
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Groq API call
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            ai_response = response.choices[0].message.content
            st.write(ai_response)

    # AI response history তে add করো
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
