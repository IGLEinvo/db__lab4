# review_service.py
from .general_service import GeneralService
from ..dao import review_dao


class ReviewService(GeneralService):
    _dao = review_dao

    def find_all_reviews(self):
        return self._dao.find_all_reviews()

    def find_review_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_review(self, review):
        return self._dao.create(review)

    def create_all_reviews(self, review_list):
        return self._dao.create_all(review_list)

    def update_review(self, key, new_review):
        return self._dao.update(key, new_review)

    def find_reviews_by_movie_id(self, movie_id):
        return self._dao.find_reviews_by_movie_id(movie_id)

    def patch_review(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_review(self, key):
        return self._dao.delete(key)

    def delete_all_reviews(self):
        return self._dao.delete_all()
