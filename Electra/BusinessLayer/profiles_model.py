
class ProfileModel:
    def __init__(self, profile_id, email, password, user_id):
        self.__id = profile_id
        self.__email = email
        self.__password = password
        self.__user_id = user_id


    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        if type(new_id) == int:
            self.__id = new_id


    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if type(new_email) == str:
            self.__email = new_email


    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if type(new_password) == str:
            self.__password = new_password


    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        if type(user_id) == int:
            self.__user_id = user_id
