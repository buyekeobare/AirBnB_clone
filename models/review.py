#!/usr/bin/python3
"""This module defines a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing review objects that
    initializes an instance of the BaseModel class"""

    place_id = ""
    user_id = ""
    text = ""
