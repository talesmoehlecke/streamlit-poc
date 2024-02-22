from .database import Database
from datetime import datetime

class Process:
    """
    Manages process operations in the MongoDB database, including creating processes.

    Attributes:
        collection (Collection): The MongoDB collection for processes.
    """

    def __init__(self):
        """
        Initializes the Process class with the 'processes' collection.
        """
        self.collection = Database().get_collection('processes')

    def create_process(self, lawyer_id, client_id, process_type, description, required_documents, status):
        """
        Creates a new legal process in the database.

        Parameters:
            lawyer_id (str): The ID of the lawyer responsible for the process.
            client_id (str): The ID of the client involved in the process.
            process_type (str): The type of the process (e.g., 'Labor', 'Civil').
            description (str): A brief or detailed description of the process.
            required_documents (list of str): A list of types of documents required for the process.
            status (str): The current status of the process (e.g., 'Open', 'In Progress', 'Completed').

        Returns:
            ObjectId: The ID of the created process.
        """
        process = {
            "lawyer_id": lawyer_id,
            "client_id": client_id,
            "process_type": process_type,
            "description": description,
            "required_documents": required_documents,
            "status": status,
            "creation_date": datetime.now(),
            "last_update": datetime.now()
        }
        return self.collection.insert_one(process).inserted_id
