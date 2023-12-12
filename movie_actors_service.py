# movieactors_service.py
from .general_service import GeneralService
from ..dao import movieactors_dao


class MovieActorsService(GeneralService):
    _dao = movieactors_dao

    def find_all_movie_actors(self):
        return self._dao.find_all_movie_actors()

    def find_movie_actor_by_ids(self, actor_id, movie_id):
        return self._dao.find_movie_actor_by_ids(actor_id=actor_id, movie_id=movie_id)

    def create_movie_actor(self, movie_actors):
        return self._dao.create_movie_actor(movie_actors)

    def create_all_movie_actors(self, movie_actors_list):
        return self._dao.create_all_movie_actors(movie_actors_list)

    def delete_movie_actor(self, actor_id, movie_id):
        return self._dao.delete_movie_actor(actor_id=actor_id, movie_id=movie_id)

    def delete_all_movie_actors(self):
        return self._dao.delete_all_movie_actors()

    def delete_by_ids(self, actor_id, movie_id):
        return self._dao.delete_by_ids(actor_id=actor_id, movie_id=movie_id)