#!/usr/bin/python3
"""
Module contains the class BaseModel that defines all common attributes/
methods for other classes
"""
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel

        Args:
            args (Tuple): all arguments passed to the object.
            kwargs (dict): dictionary that contains all arguments by key/value
        """
        if (kwargs is not None):
            for key, value in kwargs.items():
                if key != '__Class__':
                    setattr(self, key, value)

                if kwargs.get('created_at', None) is not None and
                type(kwargs['created_at']) is str:
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], time_format)
                else:
                    self.created_at = datetime.datetime.now()

                if kwargs.get('updated_at', None) is not None and
                type(kwargs['updated_at']) is str:
                    self.created_at = datetime.strptime(
                        kwargs['updated_at'], time_format)
                else:
                    self.updated_at = datetime.datetime.now()

                if (kwargs.get('id', None) is None:
                    self.id=str(uuid.uuid4())

     def __str__(self):
        """
        Returns the string representation of the current instance
        """
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        self.updated_a=datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance with 'simple
        object types'.

        Includes all keys/values of '__dict__' of the instance,
        including the '__class__' key with the class name.
        'created_at' and 'updated_at' are converted to string objects in ISO
        format.
        """
        obj_dict=self.__dict__.copy()
        obj_dict['__class__']=self.__class__.__name__

        for key, value in obj_dict.items():
            if isinstance(value, datetime.datetime):
                obj_dict[key =value.isoformat()

        return {k: v for k, v in obj_dict.items() if v is not None}
