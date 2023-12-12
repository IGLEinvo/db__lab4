from .general_dao import GeneralDAO
from ..domain import Movie


class MovieDAO(GeneralDAO):
    _domain_type = Movie

    def find_all_movies(self):
        movies = self.find_all()
        print(f"Found movies: {movies}")
        return movies

    def find_movie_by_id(self, movie_id):
        return self.find_by_id(movie_id)

    def create_movie(self, movie):
        return self.create(movie)

    def create_all_movies(self, movie_list):
        return self.create_all(movie_list)

    def update_movie(self, movie_id, updated_movie):
        return self.update(movie_id, updated_movie)

    def patch_movie(self, movie_id, field_name, value):
        return self.patch(movie_id, field_name, value)

    def delete_movie(self, movie_id):
        return self.delete(movie_id)

    def delete_all_movies(self):
        return self.delete_all()
