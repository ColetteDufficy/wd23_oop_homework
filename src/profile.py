class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []
        
        
    def add_to_favourite(self, movie):
        self.favourites.append(movie)
        
    def num_of_favourite_movies(self):
        return len(self.favourites)
        
    def remove_from_favourite(self, movie):
        self.favourites.remove(movie)
    
    def get_list_of_favourites(self):
        return self.favourites
    
    # def get_list_of_favourite_titles(self, movie):
    #     return self.favourites(movie.title)
    
    # def remove_from_favourites_by_title(self, movie):
    #     movie_to_remove = input("What movie do you want to remove?" )
    #     for movie in self.favourites:
    #         if movie_to_remove != None:
    #             self.favourites.remove(movie)
    #             return self.favourites