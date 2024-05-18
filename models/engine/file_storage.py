#!/usr/bin/python3

"""file_storage

Module contains the FileStorage Class, it's methods and attributes.
Responsible for serializing and deserializing user data for the
application.

"""

from json import dump, load

class FileStorage():
    """
    File storageclass for saving and persisting user data.
    ensurinng user data exists after each session.

    Class attributes:
    __file_path - contains path to storage json file.
    __objects- dictionary that stores all dict instances
    of base_class.
    """

    __file_path = file.json
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj inside __objects"""
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (path: __file_path)
        """

        new_dict = {}

        with open(FileStorage.__file_pa....th, "w", encoding-"utf-8") as fjason:
            for key, value in FileStorarge.__objects.items():
                new_dict[key] = value.to_dict()
                jason.dump(new_dict, fjason)
