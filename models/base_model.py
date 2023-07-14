#!/usr/bin/python3
"""
In this module we describe a basemodel class for all models in our AirBnB_clone

=======
Module contains the class BaseModel that defines all common attributes/
methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A basemodel class for all Airmodels models
    
    """
    def __init__(self, *args, **kwargs):
        """
        new model has been instatiated
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
=======
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
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

                if kwargs.get('created_at', None) is not None and\
                    type(kwargs['created_at']) is str:
                        self.created_at = datetime.strptime(
                            kwargs['created_at'], time_format)
                else:
                    self.created_at = datetime.datetime.now()

                if kwargs.get('updated_at', None) is not None and\
                    type(kwargs['updated_at']) is str:
                        self.created_at = datetime.strptime(
                            kwargs['updated_at'], time_format)
                else:
                    self.updated_at = datetime.datetime.now()

                if (kwargs.get('id', None)) is None:\
                    self.id=str(uuid.uuid4())

    def __str__(self):
        """
        returns a string model of the instance
        """
<<<<<<< HEAD
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary      
=======
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates public instance attribute 'updated_at' with current datetime
        """
        self.updated_a = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary representation of the instance with 'simple
        object types'.

        Includes all keys/values of '__dict__' of the instance,
        including the '__class__' key with the class name.
        'created_at' and 'updated_at' are converted to string objects in ISO
        format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for key, value in obj_dict.items():
            if isinstance(value, datetime.datetime):
                obj_dict[key] = value.isoformat()

        return {k: v for k, v in obj_dict.items() if v is not None}
