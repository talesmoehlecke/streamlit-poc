import yaml
from yaml.loader import SafeLoader

config_file_path = r'C:\Projeetos\wolfas\app\auth\config.yaml'
def load_config():
    with open(config_file_path) as file:
        return yaml.load(file, Loader=SafeLoader)
    
def add_users_to_config(config, user_list):
    """
    Adds a list of users to the credentials dictionary in the configuration.
    """
    for user in user_list:
        username = user.get('username')
        password_hash = user.get('password_hash')
        user_info = {       
            "email": user.get('email'),
            "logged_in": False,
            "name": user.get('name'),
            "password": password_hash
        }       
        config['credentials']['usernames'][username] = user_info