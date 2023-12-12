from .general_controller import GeneralController
from ..service import movie_service


class MovieController(GeneralController):
    _service = movie_service

    def find_all_movies(self):
        return self.find_all()

    def find_movie_by_id(self, key):
        return self.find_by_id(key)

    def create_movie(self, movie):
        return self.create(movie)

    def create_all_movies(self, movie_list):
        return self.create_all(movie_list)

    def update_movie(self, key, new_movie):
        return self.update(key, new_movie)

    def patch_movie(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_movie(self, key):
        return self.delete(key)

    def delete_all_movies(self):
        return self.delete_all()
