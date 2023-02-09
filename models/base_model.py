#! usr/bin/python3
"""base_model module"""

import uuid
from datetime import datetime

class BaseModel():
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """constructor
        Args:
            none
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """Attribute method
        prints class name
        Instance Id
        Dict representation of instance attributes
        """
        return "[{}] ({}) {}".format(self.__class__.__name, self.id, self.__dict__)

    def save(self):
        """save
        Updates attribute Updated_at with current date and time
        """
        self.updated_at = datetime.now

    def to_dict(self):
        """
        returns a dictionary containing all key/values of __dict__
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = datetime.isoformat(self.created_at)
        dict_copy["updated_at"] = datetime.isoformat(self.updated_at)

        return dict_copy

