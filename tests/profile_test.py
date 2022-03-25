import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")


    # Test a Profile can add a favourite Movie
    def test_add_a_movie_to_favourites(self):
        self.profile_1.add_to_favourite(self.movie_1)
        self.assertEqual(1, self.profile_1.num_of_favourite_movies())

    # Test a Profile can remove a given Movie from favourites
    def test_to_remove_movie_from_favourites(self):
        self.profile_1.add_to_favourite(self.movie_1)
        self.profile_1.add_to_favourite(self.movie_2)
        self.profile_1.remove_from_favourite(self.movie_1)
        self.assertEqual(1, self.profile_1.num_of_favourite_movies())
# can i return a list of the movie names????? ***************
        
    # Test a Profile can return a list of Favourites
    def test_list_of_favourite_movies(self):
        self.profile_1.add_to_favourite(self.movie_2)
        self.assertEqual([self.movie_2], self.profile_1.get_list_of_favourites())
# can i return a list of the movie names????? ***************


    
