import streamlit as st
from send_email import send_email

st.header("Contact Me ✍❤️")

with st.form(key="contact_form"):
    user_email = st.text_input("Your Email", help="I will contact you through this email")
    topic = st.selectbox("Topic you want to discuss", ["Develop  a Tech Solution", "Consult about AI & Machine Learning", "Other"])
    message = st.text_area("Message",help = "Please enter your message here")
    button = st.form_submit_button(label="Submit", help="Submit the form")

    if button:
        send_email(message, user_email, topic)
        st.success("Thank you for contacting Me. We will get back to you soon.")