import streamlit as st
import pandas as pd
import bcrypt
from menu import menu
from mongodb.user import user_service

menu()
st.title("Clients")

with st.form(key='create_client'):
  username = st.text_input('Username', key="client_name")
  password = st.text_input('Password', key="client_password")
  password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  if st.form_submit_button('Create client'):
      user_service.create_user(username, username, username, password_hash, 'client')
      st.success('Client created!')
      
      
users_dataframe = pd.DataFrame(user_service.find_all())
users_dataframe.drop('password_hash', axis = 1)
users_dataframe = users_dataframe.drop(columns=['_id','password_hash'])

print(users_dataframe)

st.dataframe(
    users_dataframe,
    width=3000,
    # column_config={
    #     "name": "Name",
    #     "username": "Username",
    # },
    hide_index=True,
) 
