#!/usr/bin/python3
"""
initialize the modules as packages
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
