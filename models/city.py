#!/usr/bin/python3
"""
Defines city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Represents city to look for """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
