import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("main.py", label="Switch accounts")
    # st.sidebar.page_link("pages/user.py", label="Your profile")
    # if st.session_state.role in ["advogado"]:
    st.sidebar.page_link("pages/process.py", label="Process")
    st.sidebar.page_link("pages/clients.py", label="Clients")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("main.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    # if "role" not in st.session_state or st.session_state.role is None:
    if st.session_state["authentication_status"]:
        authenticated_menu()
        return
    unauthenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()