import streamlit as st
st.title("Login Page")
st.write("Please enter your credentials to login.")
login_username = st.text_input("Username")
login_password = st.text_input("Password", type="password")
if st.button("Login"):
    if login_username == username and login_password == password:
        st.success("Login successful!")
    else:
        st.error("Invalid username or password!")