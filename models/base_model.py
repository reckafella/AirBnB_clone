#!/usr/bin/python3
"""
In this module we describe a basemodel class for all models in our AirBnB_clone

"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    A BaseModel class for all AirBnB_clone model
    """
    time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        new model has is instatiated
        """
        if not kwargs:
            if args:
                pass
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     self.time_format)
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     self.time_format)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        returns a string model of the instance
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
       """
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
