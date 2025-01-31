from Electra.DataAccessLayer.users_profiles import UsersProfiles
from Electra.BusinessLayer.profiles_model import ProfileModel

class ProfilesService:

    def get_all_profiles(self):
        profile = UsersProfiles()
        profiles_list = [profile.read_all_profiles()]
        for row in profiles_list:
            model = ProfileModel(profile_id=row[0], email=row[1], password=row[2], user_id=row[3])
        return profiles_list


    def update_profile(self, model):
        profile = UsersProfiles()
        profiles = profile.update_profile(model)
        return profiles

    def add_profile(self, model):
        profile = UsersProfiles()
        profile.create_profile(model)

    def delete_profile(self, model):
        profile = UsersProfiles()
        profile.delete_profile(model)

    def check_profile(self, model, index):
        profile = UsersProfiles()
        return profile.check_profile(model, index)

