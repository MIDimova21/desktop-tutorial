from Electra.DataAccessLayer.users import Users
from Electra.BusinessLayer.user_model import UserModel

class UserService:

    def get_all_users(self):
        user = Users()
        users_list = [user.read_all_users()]
        for row in users_list:
            model = UserModel(user_id=row[0], first_name=row[1], last_name=row[2], age=row[3])
        return users_list

    def get_user_by_id(self, model):
        user = Users()
        found_user = user.read_user_by_id(model.get_id)
        return found_user

    def update_user(self, model):
        user = Users()
        users = user.update_user(model)
        return users

    def add_user(self, model):
        user = Users()
        user.create_user(model)

    def delete_user(self, model):
        user = Users()
        user.delete_user(model)

