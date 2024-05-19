#!/usr/bin/python3

from .base_model import BaseModel
from .user import User

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
