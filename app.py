
import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh 

# Initialize session state for navigation and inputs
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"  # Default page

if "username" not in st.session_state:
    st.session_state.username = ""

if "room_name" not in st.session_state:
    st.session_state.room_name = ""

if "room_id" not in st.session_state:
    st.session_state.room_id = "default_room"  # Default room ID

# Function to navigate between pages
def navigate_to(page_name):
    st.session_state.current_page = page_name

def fetch_messages():
    response = requests.get(f"http://127.0.0.1:8000/get_messages/{st.session_state.room_id}")
    if response.status_code == 200:
        return response.json().get("messages", [])
    return []


# Use a placeholder to dynamically render the active page
page_placeholder = st.empty()

# Render only the active page
with page_placeholder.container():
    if st.session_state.current_page == "Home":
        # Home Page Logic
        st.title("Chat Box")

        # Inputs for room name and username
        Room_Name = st.text_input("Room Name")
        Username = st.text_input("Username")

        # Enter Room Button
        if st.button("Enter Room"):
            if not Room_Name.strip():
                st.error("Room Name cannot be empty!")
            elif not Username.strip():
                st.error("Username cannot be empty!")
            else:
                # Data to send to the backend
                data = {
                    "room_name": Room_Name.strip(),
                    "username": Username.strip(),
                }

                # Send request to the backend
                response = requests.post("http://127.0.0.1:8000/checkview", data)

                if response.status_code == 200:
                    # Save data in session state and navigate
                    st.session_state.room_name = Room_Name.strip()
                    st.session_state.username = Username.strip()
                    navigate_to("Chat Room")
                else:
                    st.error("Failed to enter room. Please try again.")

    elif st.session_state.current_page == "Chat Room":
        # Room Page Logic
        st.title(f"Welcome to Room: {st.session_state.room_name}")
        st.text(f"Username: {st.session_state.username}")

        st_autorefresh(interval=5000, key="chat_autorefresh")

        response2 = requests.get(f"http://127.0.0.1:8000/getMessages/{st.session_state.room_name}/")
        response_data2 = response2.json()
        # print(response_data2)
        user_colors = {"Harshith": "#007BFF", "Harshini": "#FF5733"}  # Customize colors per user
        default_color = "#000000"  # Default text color (black)
        # st.json(response_data2)
        for message in response_data2['messages']:
            user_color = user_colors.get(message['user'], default_color)  # Fetch color for user or use default

            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ddd; 
                    padding: 10px; 
                    margin-bottom: 10px; 
                    border-radius: 5px; 
                    background-color: #f9f9f9;">
                    <strong style="color: {user_color};">{message['user']}:</strong>
                    <span style="color: #2C3E50;">{message['value']}</span><br>
                    <small style="color: gray;"><i>{message['date']}</i></small>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Chat input
        with st.form("chat_form", clear_on_submit=True):
            message = st.text_input("Type your message:")
            send_button = st.form_submit_button("Send")
            if send_button:
                if message.strip():
                    # Placeholder for sending the message to the backend
                    response1 = requests.get(f"http://127.0.0.1:8000/getroom/{st.session_state.room_name}/")
                    response_data = response1.json()
                    room_id = response_data.get("room_id")

                    response = requests.post("http://127.0.0.1:8000/send", data= {"message":message, "username": {st.session_state.username},"room_id": room_id})
                    # if response.status_code == 200:
                    #     st.success(f"Message sent: {message}")
                    # else:
                    #     st.error(f"not add to db {room_id}")
                else:
                    st.error("Message cannot be empty!")

        # Leave Room Button
        if st.button("Leave Room"):
            navigate_to("Home")


# import streamlit as st
# import os
# import requests


# # # harsh_endpoint = "http://127.0.0.1:8000/"
# # requests.get("http://127.0.0.1:8000/")
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "Home"  # Default page

# if "username" not in st.session_state:
#     st.session_state.username = ""
# if "room_name" not in st.session_state:
#     st.session_state.room_name = ""

# def navigate_to(page_name,dict = None):
#     st.session_state.current_page = page_name

# if st.session_state.current_page == "Home":

#     st.title("Chat Box")

#     Room_Name = st.text_input("Room Name")
#     Username = st.text_input("Username")

#     if st.button("Enter Room"):
#         data = {
#             "room_name" : Room_Name,
#             "username" : Username
            
#         }
#         response = requests.post("http://127.0.0.1:8000/checkview",data)
        
#         if response.status_code == 200:
#             navigate_to("Chat room",data)
#             st.success("Succesfully Entered room")
#         else:
#             st.error("Failed to enter room")

# elif st.session_state.current_page == "Chat room":
    
#     message = st.text_input("Type")


# import streamlit as st
# import requests

# # Initialize session state for navigation and inputs
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "Home"  # Default page

# if "username" not in st.session_state:
#     st.session_state.username = ""

# if "room_name" not in st.session_state:
#     st.session_state.room_name = ""

# # Function to navigate between pages
# def navigate_to(page_name):
#     st.session_state.current_page = page_name

# render = True

# while render :
#     # Home Page Logic
#     if st.session_state.current_page == "Home":
#         st.title("Chat Box")

#         # Inputs for room name and username
#         Room_Name = st.text_input("Room Name")
#         Username = st.text_input("Username")

#         # Enter Room Button
#         if st.button("Enter Room"):
#             if not Room_Name.strip():
#                 st.error("Room Name cannot be empty!")
#             elif not Username.strip():
#                 st.error("Username cannot be empty!")
#             else:
#                 # Data to send to the backend
#                 data = {
#                     "room_name": Room_Name.strip(),
#                     "username": Username.strip(),
#                 }

#                 # Send request to the backend
#                 response = requests.post("http://127.0.0.1:8000/checkview", data)

#                 if response.status_code == 200:
#                     # Save data in session state and navigate
#                     st.session_state.room_name = Room_Name.strip()
#                     st.session_state.username = Username.strip()
#                     navigate_to("Chat room")
#                     st.success("Successfully entered the room!")
#                 else:
#                     st.error("Failed to enter room. Please try again.")
#                     render = False

#     # Chat Room Logic
#     elif st.session_state.current_page == "Chat room":
#         st.empty()
#         st.title(f"Welcome to Room: {st.session_state.room_name}")
#         st.text(f"Username: {st.session_state.username}")

#         # Chat input
#         message = st.text_input("Type your message:")
#         if st.button("Send"):
#             if message.strip():
#                 # Placeholder for sending the message to the backend
#                 st.success(f"Message sent: {message}")
#             else:
#                 st.error("Message cannot be empty!")

#         # Leave Room Button
#         if st.button("Leave Room"):
#             navigate_to("Home")


# import streamlit as st
# import requests

# # Initialize session state for navigation and inputs
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "Home"  # Default page

# if "username" not in st.session_state:
#     st.session_state.username = ""

# if "room_name" not in st.session_state:
#     st.session_state.room_name = ""

# # Function to navigate between pages
# def navigate_to(page_name):
#     st.session_state.current_page = page_name

# # Use a placeholder to dynamically render the active page
# page_placeholder = st.empty()

# # Render only the active page
# with page_placeholder.container():
#     if st.session_state.current_page == "Home":
#         # Home Page Logic
#         st.title("Chat Box")

#         # Inputs for room name and username
#         Room_Name = st.text_input("Room Name")
#         Username = st.text_input("Username")

#         # Enter Room Button
#         if st.button("Enter Room"):
#             if not Room_Name.strip():
#                 st.error("Room Name cannot be empty!")
#             elif not Username.strip():
#                 st.error("Username cannot be empty!")
#             else:
#                 # Data to send to the backend
#                 data = {
#                     "room_name": Room_Name.strip(),
#                     "username": Username.strip(),
#                 }

#                 # Send request to the backend
#                 response = requests.post("http://127.0.0.1:8000/checkview", data)

#                 if response.status_code == 200:
#                     # Save data in session state and navigate
#                     st.session_state.room_name = Room_Name.strip()
#                     st.session_state.username = Username.strip()
#                     navigate_to("Chat Room") 
#                 else:
#                     st.error("Failed to enter room. Please try again.")

#     elif st.session_state.current_page == "Chat Room":
#         # Room Page Logic
#         st.title(f"Welcome to Room: {st.session_state.room_name}")
#         st.text(f"Username: {st.session_state.username}")

#         # Chat input
#         message = st.text_input("Type your message:")
#         if st.button("Send"):
#             if message.strip():
#                 # Placeholder for sending the message to the backend
#                 st.success(f"Message sent: {message}")
#             else:
#                 st.error("Message cannot be empty!")

#         # Leave Room Button
#         if st.button("Leave Room"):
#             navigate_to("Home")
