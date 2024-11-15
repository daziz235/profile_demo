import streamlit as st
import requests
import re



def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            

            if not name:
                st.error("Please provide your name.", icon = "🧑🏼‍🦲")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon = "📧")
                st.stop()

            if not is_valid_email(email):
                st.error("PPlease provide a valid email address.", icon = "✉️")
                st.stop()

            if not message:
                st.error("Please provide a message.", icon = "💬")
                st.stop()

            
            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon= "🥳")
            else:
                st.error("There was an error sending your message.", icon ="☹️")



