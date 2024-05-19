#!/usr/bin/python3
"""This module defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing user objects that
  initializes an instance of the BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
