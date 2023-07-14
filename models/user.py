#!/usr/bin/python3
"""
This file module describes a class User

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class describes a 'User' by listed attributes
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
