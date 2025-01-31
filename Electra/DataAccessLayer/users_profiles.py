from Electra.DataAccessLayer.connection import *
from Electra.BusinessLayer.profiles_model import *


class UsersProfiles:
    def __init__(self):
        self.connect = Connection()
        self.connection = self.connect.connection


    def read_all_profiles(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Users_Profiles')
        data = cursor.fetchall()
        profile_list = []
        for row in data:
            profile = ProfileModel(profile_id=row[0], email=row[1], password=row[2], user_id=row[3])
            profile_list.append(profile)
        return profile_list

    def create_profile(self,profile):
        cursor = self.connection.cursor()
        query = "Insert into Users_Profiles (profile_id, email, password, user_id) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (profile.get_id(), profile.get_email(), profile.get_password(), profile.get_user_id()))
        self.connection.commit()

    def update_profile(self,profile):
        cursor = self.connection.cursor()
        cursor.execute("Update Users_Profiles set email = ? where profile_id = ?", (profile.get_email(), profile.get_id()))
        cursor.execute("Update Users_Profiles set password = ? where profile_id = ?", (profile.get_password(), profile.get_id()))
        self.connection.commit()

    def delete_profile(self,profile):
        cursor = self.connection.cursor()
        query = "Delete from Users_Profiles where profile_id = ?"
        cursor.execute(query, profile.get_id())
        self.connection.commit()


    def check_profile(self, check, index):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Users_Profiles')
        data = cursor.fetchall()
        for row in data:
            if check == row[index]:
                return True
        return False

