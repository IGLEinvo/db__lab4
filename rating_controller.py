# rating_controller.py
from .general_controller import GeneralController
from ..service import rating_service


class RatingController(GeneralController):
    _service = rating_service

    def find_all_ratings(self):
        return self.find_all()

    def find_rating_by_id(self, key):
        return self.find_by_id(key)

    def create_rating(self, rating):
        return self.create(rating)

    def create_all_ratings(self, rating_list):
        return self.create_all(rating_list)

    def update_rating(self, key, new_rating):
        return self.update(key, new_rating)

    def patch_rating(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_rating(self, key):
        return self.delete(key)

    def delete_all_ratings(self):
        return self.delete_all()
