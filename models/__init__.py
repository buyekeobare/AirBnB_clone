#!/usr/bin/python3
"""This script initializes the package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
