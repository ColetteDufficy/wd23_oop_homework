
class Account:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profiles_list = []
        
    
    def add_profile(self, profile):
        self.profiles_list.append(profile)

    def remove_profile(self, profile):
        self.profiles_list.remove(profile)
        
    def list_all_profiles(self):
        return self.profiles_list
