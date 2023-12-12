# rating_service.py
from .general_service import GeneralService
from ..dao import rating_dao


class RatingService(GeneralService):
    _dao = rating_dao

    def find_all_ratings(self):
        return self._dao.find_all_ratings()

    def find_rating_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_rating(self, rating):
        return self._dao.create(rating)

    def create_all_ratings(self, rating_list):
        return self._dao.create_all(rating_list)

    def update_rating(self, key, new_rating):
        return self._dao.update(key, new_rating)

    def patch_rating(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_rating(self, key):
        return self._dao.delete(key)

    def delete_all_ratings(self):
        return self._dao.delete_all()
