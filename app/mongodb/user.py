from .database import Database
from datetime import datetime
from bson import binary
from dataclasses import dataclass

@dataclass
class User:
    username: str
    name: str
    email: str
    password_hash: str
    user_type: str
    creation_date: datetime = datetime.now()
    
    
class UserService:
    """
    A class to manage user operations in the MongoDB database, including creating users.

    Attributes:
        collection (Collection): The MongoDB collection for users.
    """

    def __init__(self):
        """
        Initializes the User class with the 'users' collection.
        """
        self.collection = Database().get_collection('users')

    def create_user(self, username, name, email, password_hash, user_type):
        """
        Creates a new user in the database.

        Parameters:
            username (str): Username.
            name (str): The full name of the user.
            email (str): The email address of the user.
            password (str): The password for the user (will be hashed before storage).
            user_type (str): The type of the user (e.g., 'client', 'lawyer').

        Returns:
            ObjectId: The ID of the created user document.
        """
        user = {
            "username": username,
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "user_type": user_type,
            "creation_date": datetime.now()
        }
        
        return self.collection.insert_one(user).inserted_id

    
    def find_by_email(self, email):
        """
        Finds a user by their email.

        Parameters:
            email (str): The email address of the user.

        Returns:
            User: user found
        """
        return self.collection.find_one({"email": email})
    
    def find_all(self):
        return list(self.collection.find())
    
    def change_password(self, username, new_password_hash):
        """
        Changes the password for a user identified by their username.
    
        Parameters:
            username (str): The username of the user.
            new_password_hash (str): The new hashed password to set for the user.
    
        Returns:
            bool: True if the password was successfully changed, False otherwise.
        """
        # Atualizar a senha do usuário no banco de dados
        updated_result = self.collection.update_one(
            {"username": username},
            {"$set": {"password_hash": new_password_hash}}
        )
    
        # Verificar se a senha foi alterada com sucesso
        return updated_result.modified_count > 0

user_service = UserService()