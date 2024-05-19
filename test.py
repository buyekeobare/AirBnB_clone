#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

def create_instance():

    model = BaseModel()
    print('Basemodel created')
    user = User()
    print('user created')

def main():
    print('about to create instances')
    create_instance()

if __name__ == '__main__':
    main()
