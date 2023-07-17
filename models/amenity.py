#!/usr/bin/python
"""
Defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents Amenities that user can choose from to offer at its place"""
    name = ""
