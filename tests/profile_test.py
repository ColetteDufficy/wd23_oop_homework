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
        self.profile_1.add_to_favourite(self.movie_2)
        self.assertEqual([self.movie_1, self.movie_2], self.profile_1.get_list_of_favourites())   #this returns a list of movies
        self.assertEqual(2, self.profile_1.num_of_favourite_movies())   #this returns the number of movies in the 'favourites' list
         

    # Test a Profile can remove a given Movie from favourites
    def test_to_remove_movie_from_favourites(self):
        self.profile_1.add_to_favourite(self.movie_1)
        self.profile_1.add_to_favourite(self.movie_2)
        self.profile_1.remove_from_favourite(self.movie_1)
        self.assertEqual(1, self.profile_1.num_of_favourite_movies())
        
 
    # Test a Profile can return a list of Favourites
    def test_list_of_favourite_movies(self):
        self.profile_1.add_to_favourite(self.movie_2)
        self.assertEqual([self.movie_2], self.profile_1.get_list_of_favourites())
# can i return a list of the movie names? ***************



    # # **** MY OWN TEST - Test a Profile can return a list of Favourites by titles 
    # def test_add_a_movie_to_favourites_by_title(self):
    #     # breakpoint()
    #     self.profile_1.add_to_favourite(self.movie_1)
    #     self.profile_1.add_to_favourite(self.movie_2)
    #     self.assertEqual(["The Fugitive", "Hunger Games"], self.profile_1.get_list_of_favourite_titles(self.movie_1.title, self.movie_2.title))
    #     # is this wwhere you cant acesss the list contents of aaother class, becasue you shouldnt be able to see into it??? so im never going to be able to see it???????
    
    
    # def test_to_remove_movie_from_favourites(self):
    #     self.profile_1.add_to_favourite(self.movie_1)
    #     self.profile_1.add_to_favourite(self.movie_2)
    #     self.profile_1.remove_from_favourites_by_title(self.movie_1)
    #     self.assertEqual([self.movie_2], self.profile_1.get_list_of_favourites(self.movie_2))