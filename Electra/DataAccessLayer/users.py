from Electra.DataAccessLayer.connection import *
from Electra.BusinessLayer.user_model import *


class Users:
    def __init__(self):
        self.connect = Connection()
        self.connection = self.connect.connection


    def read_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Users')
        data = cursor.fetchall()
        user_list = []
        for row in data:
            user = UserModel(user_id=row[0], first_name=row[1], last_name=row[2], age=row[3])
            user_list.append(user)
        return user_list

    def create_user(self,user):
        cursor = self.connection.cursor()
        query = "Insert into Users (user_id, first_name, last_name, age) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (user.get_id(), user.get_first_name(), user.get_last_name(), user.get_age()))
        self.connection.commit()

    def update_user(self,user):
        cursor = self.connection.cursor()
        cursor.execute("Update Users set age = ? where user_id = ?", (user.get_age(), user.get_id()))
        cursor.execute("Update Users set first_name = ? where user_id = ?", (user.get_first_name(), user.get_id()))
        cursor.execute("Update Users set last_name = ? where user_id = ?", (user.get_last_name(), user.get_id()))
        self.connection.commit()

    def delete_user(self,user):
        cursor = self.connection.cursor()
        query = "Delete from Users where user_id = ?"
        cursor.execute(query, user.get_id())
        self.connection.commit()


    def read_user_by_id(self, user):
        cursor = self.connection.cursor()
        query = "Select * from Users where user_id = ?"
        cursor.execute(query, user.get_id())
        data = cursor.fetchone()
        return data
