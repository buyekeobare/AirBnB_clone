#!/usr/bin/python3

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
