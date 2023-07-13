#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    """ Defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """
        Returns the string representation of the current instance
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance with 'simple object types'.
        Includes all keys/values of '__dict__' of the instance, 
        including the '__class__' key with the class name.
        'created_at' and 'updated_at' are converted to string objects in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for key, value in obj_dict.items():
            if isinstance(value, datetime.datetime):
                obj_dict[key] = value.isoformat()
        
        return {k: v for k, v in obj_dict.items() if v is not None}
                
