# import streamlit as st
# st.title("Hello, Streamlit!")

# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()

import streamlit as st
import os

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Function to load HTML content
def load_html_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h3>File not found: {file_path}</h3>"

# Function to handle HTML button clicks
def handle_html_buttons():
    # Check for button clicks in query parameters
    query_params = st.query_params()
    if "navigate" in query_params:
        if query_params["navigate"][0] == "Room":
            st.session_state.current_page = "Room"

# Check and handle HTML button clicks
handle_html_buttons()

# Render pages based on the current state
if st.session_state.current_page == "Home":
    st.title("Home Page")
    
    # Load and display the home.html file
    html_file_path_home = os.path.join(os.getcwd(), 'home.html')
    html_content_home = load_html_file(html_file_path_home)
    
    st.components.v1.html(html_content_home, height=500)

elif st.session_state.current_page == "Room":
    st.title("Room Page")
    
    # Load and display the room.html file
    html_file_path_room = os.path.join(os.getcwd(), 'room.html')
    html_content_room = load_html_file(html_file_path_room)
    
    st.components.v1.html(html_content_room, height=500)
