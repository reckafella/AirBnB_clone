#!/usr/bin/python3
from models.base_model import BaseModel
""" Review to inherit from BaseModel module"""
class Review(BaseModel):
    """The review class"""
    place_id = ''
    user_id = ''
    text = ''
