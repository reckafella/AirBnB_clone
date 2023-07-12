#!/usr/bin/python3
"""
Module contains a class BaseModel that defines all common
attributes/methods for other classes
"""
import uuid
import datetime

class BaseModel(uuid, datetime):
    """ Defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str('')
        self.updated_at = str('')
    
    def __str__(self):
        """
        Prints the current instance of the class
        """
        str_object = '{[]} {()} {}'.format(self.__class__.__name__, self.id, self.__dict__)
        print(str_object)

    def __dict__(self):
        """
        Dictionary representation of the current instance
        """
        pass

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        pass

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of '__dict__' of the
        instance.
        """
        pass
