# movieactors_dao.py
from .general_dao import GeneralDAO
from ..domain import MovieActors


class MovieActorsDAO(GeneralDAO):
    _domain_type = MovieActors

    def find_all_movie_actors(self):
        movie_actors = self.find_all()
        print(f"Found movie actors: {movie_actors}")
        return movie_actors

    def find_movie_actor_by_ids(self, actor_id, movie_id):
        return self.find_by_ids(actor_id=actor_id, movie_id=movie_id)

    def create_movie_actor(self, movie_actors):
        return self.create(movie_actors)

    def create_all_movie_actors(self, movie_actors_list):
        return self.create_all(movie_actors_list)

    def delete_movie_actor(self, actor_id, movie_id):
        return self.delete_by_ids(actor_id=actor_id, movie_id=movie_id)

    def delete_by_ids(self, actor_id, movie_id):
        movie_actor = self._domain_type.query.filter_by(actor_id=actor_id, movie_id=movie_id).first()
        if movie_actor:
            self.delete(movie_actor)
            return True
        return False
    def delete_all_movie_actors(self):
        return self.delete_all()
