import streamlit as st
import streamlit_authenticator as stauth
import yaml
import base64
from yaml.loader import SafeLoader
from mongodb.user import User
from auth.config import load_config, add_users_to_config
from widgets import register_widget, change_password_widget

#AUTHENTICATION
user_service = User()
config = load_config()
add_users_to_config(config, user_service.find_all())

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()
#END

        
if st.session_state["authentication_status"]:
    #authenticated menu
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    change_password_widget(user_service, authenticator)
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    register_widget(user_service, authenticator)
    
    # FORGOT PASSWORD
    # try:
    #     username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    #     if username_of_forgotten_password:
    #         st.success('New password to be sent securely')
    #         # The developer should securely transfer the new password to the user.
    #     elif username_of_forgotten_password == False:
    #         st.error('Username not found')
    # except Exception as e:
    #     st.error(e)