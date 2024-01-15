#!/usr/bin/python3
"""Initialization magic method for the 'models' directory."""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage for data storage
data_storage = FileStorage()

# Reload data from storage to populate the instance with existing data
data_storage.reload()
