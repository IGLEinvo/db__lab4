from .general_service import GeneralService
from ..dao import movie_dao


class MovieService(GeneralService):
    _dao = movie_dao

    def find_all_movies(self):
        return self._dao.find_all_movies()

    def find_movie_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_movie(self, movie):
        return self._dao.create(movie)

    def create_all_movies(self, movie_list):
        return self._dao.create_all(movie_list)

    def update_movie(self, key, new_movie):
        return self._dao.update(key, new_movie)

    def patch_movie(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_movie(self, key):
        return self._dao.delete(key)

    def delete_all_movies(self):
        return self._dao.delete_all()
