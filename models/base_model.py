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
        return '{} {} {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of '__dict__' of the
        instance.
        """
        return self.__dict__
