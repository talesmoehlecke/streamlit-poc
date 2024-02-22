from .database import Database
from datetime import datetime

class Document:
    """
    Manages document operations in the MongoDB database, including creating documents.

    Attributes:
        collection (Collection): The MongoDB collection for documents.
    """

    def __init__(self):
        """
        Initializes the Document class with the 'documents' collection.
        """
        self.collection = Database().get_collection('documents')

    def create_document(self, user_id, document_name, document_type, s3_url, process_id=None):
        """
        Creates a new document in the database.

        Parameters:
            user_id (str): The ID of the user associated with the document.
            document_name (str): The original name of the document.
            document_type (str): The type of the document (e.g., 'Identity', 'Residence Proof').
            s3_url (str): The S3 URL or key of the document file.
            process_id (str, optional): The ID of the process the document is related to, if any.

        Returns:
            ObjectId: The ID of the created document.
        """
        document = {
            "user_id": user_id,
            "process_id": process_id,
            "document_name": document_name,
            "document_type": document_type,
            "s3_url": s3_url,
            "upload_date": datetime.now()
        }
        return self.collection.insert_one(document).inserted_id
