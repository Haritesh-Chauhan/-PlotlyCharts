import streamlit as st
import base64
from streamlit_lottie import st_lottie

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def set_bg_from_local(image_file):
    encoded_string = get_base64_of_image(image_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Main App ---
set_bg_from_local("F:\Images\pexels-pixabay-326055.jpg") 

st.title("My App with a Background Image")
st.write("This method is quick to implement.")


# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- Authentication Logic ---
def check_credentials(username, password):
    # This is where you would check a database or a file
    # For this example, we'll use a hardcoded username and password
    if username == "admin" and password == "password123":
        return True
    return False

def show_login_page():
    st.title("Login")
    st.write("Please enter your credentials to continue.")
    
    with st.form("login_form"):
        lottie_url = "https://lottie.host/6a7db818-bf4e-4455-98cc-4e03488c20cd/FXaYMKPXIq.json"
        if lottie_url:
            st_lottie(lottie_url, speed=1, height=200)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if check_credentials(username, password):
                st.session_state.authenticated = True
                st.rerun() # Rerun the script to show the main app
            else:
                st.error("Invalid username or password")

def show_main_page():
    st.title("Main Application")
    st.write("Welcome, you have successfully logged in!")
    st.write("This is the main content of your application.")

    # A logout button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun() # Rerun the script to show the login page

# --- Main App Flow ---
if st.session_state.authenticated:
    show_main_page()
else:
    show_login_page()