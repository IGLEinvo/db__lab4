# actor_dao.py
from .general_dao import GeneralDAO
from ..domain import Actor


class ActorDAO(GeneralDAO):
    _domain_type = Actor

    def find_all_actors(self):
        actors = self.find_all()
        print(f"Found actors: {actors}")
        return actors

    def find_actor_by_id(self, actor_id):
        return self.find_by_id(actor_id)

    def create_actor(self, actor):
        return self.create(actor)

    def create_all_actors(self, actor_list):
        return self.create_all(actor_list)

    def update_actor(self, actor_id, updated_actor):
        return self.update(actor_id, updated_actor)

    def patch_actor(self, actor_id, field_name, value):
        return self.patch(actor_id, field_name, value)

    def delete_actor(self, actor_id):
        return self.delete(actor_id)

    def delete_all_actors(self):
        return self.delete_all()
