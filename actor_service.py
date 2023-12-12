# actor_service.py
from .general_service import GeneralService
from ..dao import actor_dao


class ActorService(GeneralService):
    _dao = actor_dao

    def find_all_actors(self):
        return self._dao.find_all_actors()

    def find_actor_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_actor(self, actor):
        return self._dao.create(actor)

    def create_all_actors(self, actor_list):
        return self._dao.create_all(actor_list)

    def update_actor(self, key, new_actor):
        return self._dao.update(key, new_actor)

    def patch_actor(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_actor(self, key):
        return self._dao.delete(key)

    def delete_all_actors(self):
        return self._dao.delete_all()
