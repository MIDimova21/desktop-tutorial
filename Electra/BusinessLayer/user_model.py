
class UserModel:
    def __init__(self, user_id, first_name, last_name, age):
        self.__id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age


    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if type(new_id) == int:
            self.__id = new_id


    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        if type(new_first_name) == str:
            self.__first_name = new_first_name


    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_last_name):
        if type(new_last_name) == str:
            self.__last_name = new_last_name


    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) == int:
            self.__age = new_age