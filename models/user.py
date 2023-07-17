#!/usr/bin/python3
"""
Defines User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Defines attributes for user creation """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
