# rating_dao.py
from .general_dao import GeneralDAO
from ..domain import Rating


class RatingDAO(GeneralDAO):
    _domain_type = Rating

    def find_all_ratings(self):
        return self.find_all()

    def find_rating_by_id(self, rating_id):
        return self.find_by_id(rating_id)

    def create_rating(self, rating):
        return self.create(rating)

    def create_all_ratings(self, rating_list):
        return self.create_all(rating_list)

    def update_rating(self, rating_id, updated_rating):
        return self.update(rating_id, updated_rating)

    def patch_rating(self, rating_id, field_name, value):
        return self.patch(rating_id, field_name, value)

    def delete_rating(self, rating_id):
        return self.delete(rating_id)

    def delete_all_ratings(self):
        return self.delete_all()
