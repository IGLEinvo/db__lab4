# movie_actors_controller.py
from .general_controller import GeneralController
from ..service import movie_actors_service


class MovieActorsController(GeneralController):
    _service = movie_actors_service

    def find_all_movie_actors(self):
        return self.find_all()

    def find_movie_actor_by_ids(self, actor_id, movie_id):
        return self.find_by_ids(actor_id=actor_id, movie_id=movie_id)

    def create_movie_actor(self, movie_actor):
        return self.create(movie_actor)

    def create_all_movie_actors(self, movie_actor_list):
        return self.create_all(movie_actor_list)

    def update_movie_actor(self, actor_id, movie_id, new_movie_actor):
        return self.update_by_ids(actor_id=actor_id, movie_id=movie_id, new_obj=new_movie_actor)

    def patch_movie_actor(self, actor_id, movie_id, value_dict):
        return self.patch_by_ids(actor_id=actor_id, movie_id=movie_id, value_dict=value_dict)

    def delete_movie_actor(self, actor_id, movie_id):
        return self.delete_by_ids(actor_id=actor_id, movie_id=movie_id)

    def delete_all_movie_actors(self):
        return self.delete_all()
