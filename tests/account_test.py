import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")

        

    # Test an Account can add a Profile
    def test_add_profile_to_account(self):
        self.account_1.add_profile(self.profile_1)
        self.assertEqual("harrisonF", self.profile_1.username)

        
    # Test an Account can remove a given Profile
    def test_remove_profile_from_account(self):
        self.account_1.add_profile(self.profile_1)
        self.account_1.remove_profile(self.profile_1)
        self.assertEqual("harrisonF", self.profile_1.username)
# wud be nice to check that the profile is definetly on the account first, and it wud be even better not tore ove it entirely*****
    
    # Test an Account can return a list of Profiles
    def test_list_of_profiles_on_account(self):
        profile_3 = Profile("duffer99", "gr8p@ssword")
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        self.account_1.add_profile(profile_3)
        self.assertEqual([self.profile_1, self.profile_2, profile_3], self.account_1.get_profiles())


        
    

   
