import streamlit as st
import send_email

st.header("Contact me")

with st.form(key="contact_me"):
    user_email = st.text_input("Enter your email address here", key="user_email")
    text_input = st.text_area("Enter your text here", key="text_input")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{text_input}
    """
    button = st.form_submit_button("Send!")

    if button:
        send_email.send_email(message)
        st.info("Your email was sent successfully")


