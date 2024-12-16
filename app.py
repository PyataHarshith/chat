import streamlit as st
import os
import requests


# # harsh_endpoint = "http://127.0.0.1:8000/"
# requests.get("http://127.0.0.1:8000/")

st.title("Chat Box")

Room_Name = st.text_input("Room Name")
Username = st.text_input("Username")

if st.button("Enter Room"):
    data = {
        "room_name" : Room_Name,
        "username" : Username
        
    }
    response = requests.post("http://127.0.0.1:8000/checkview",json=data )

    if response.status_code == 200:
        st.success("Succesfully Entered room")
    else:
        st.error("Failed to enter room")