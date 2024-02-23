import streamlit as st
import streamlit_authenticator as stauth
import logging

logger = logging.getLogger(__name__)

def register_widget(user_service, authenticator):
    """
    Creates a registration widget using the Streamlit interface. This method facilitates the registration of new users
    through the Streamlit Authenticator interface. After a user is successfully registered in-memory, this method
    persists the user data to a MongoDB database.

    Parameters:
    - user_service: An instance of the user service responsible for communicating with the MongoDB database to persist user data.
    - authenticator: An instance of the Streamlit Authenticator used to manage user registration and authentication processes.

    The function captures the email, username, and full name from the registration widget. Upon successful registration,
    the user's data, including a hashed password, is persisted in the MongoDB database with the help of the user service.

    Exceptions:
    - Exception: Catches and displays any exceptions raised during the registration process or while persisting data to the database,
      using Streamlit's interface to display error messages.
    """
    try:
        # User creation through Streamlit registration widget
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            created_user = authenticator.credentials["usernames"][username_of_registered_user]
            password_hash = created_user["password"]
            user_service.create_user(username_of_registered_user, name_of_registered_user, email_of_registered_user, password_hash, "adv")
    except Exception as e:
        st.error(e)
        
def change_password_widget(user_service, authenticator):
    """
    Creates a password reset widget using the Streamlit interface. This method enables users to change their password
    through the Streamlit Authenticator interface. After a password is successfully changed in-memory, this method
    updates the user's password in the MongoDB database.

    Parameters:
    - user_service: An instance of the user service responsible for communicating with the MongoDB database to update the user's password.
    - authenticator: An instance of the Streamlit Authenticator used to manage password changes.

    The function initiates the password reset process for the currently logged-in user. If the password change is successful,
    the new hashed password is updated in the MongoDB database using the user service.

    Exceptions:
    - Exception: Catches and displays any exceptions raised during the password change process or while updating the password in the database,
      using Streamlit's interface to display error messages.
    """
    try:
        # Password reset through Streamlit password reset widget
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
            user_changed = authenticator.credentials["usernames"][st.session_state["username"]]
            password_hash = user_changed["password"]
            username = st.session_state["username"]
            user_service.change_password(username, password_hash)
    except Exception as e:
        st.error(e)