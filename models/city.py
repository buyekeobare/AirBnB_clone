#!/usr/bin/python3
"""This module defines a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing city objects that
    initializes an instance of the BaseModel class"""

    state_id = ""
    name = ""
