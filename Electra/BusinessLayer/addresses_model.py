
class AddressModel:
    def __init__(self, address_id, region, city, user_id):
        self.__id = address_id
        self.__region = region
        self.__city = city
        self.__user_id = user_id


    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if type(new_id) == int:
            self.__id = new_id


    def get_region(self):
        return self.__region

    def set_region(self, new_region):
        if type(new_region) == str:
            self.__region = new_region


    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        if type(new_city) == str:
            self.__city = new_city


    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        if type(user_id) == int:
            self.__user_id = user_id
