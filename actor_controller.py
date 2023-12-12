# actor_controller.py
from .general_controller import GeneralController
from ..service import actor_service


class ActorController(GeneralController):
    _service = actor_service

    def find_all_actors(self):
        return self.find_all()

    def find_actor_by_id(self, key):
        return self.find_by_id(key)

    def create_actor(self, actor):
        return self.create(actor)

    def create_all_actors(self, actor_list):
        return self.create_all(actor_list)

    def update_actor(self, key, new_actor):
        return self.update(key, new_actor)

    def patch_actor(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_actor(self, key):
        return self.delete(key)

    def delete_all_actors(self):
        return self.delete_all()
