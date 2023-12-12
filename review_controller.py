# review_controller.py
from .general_controller import GeneralController
from ..service import review_service


class ReviewController(GeneralController):
    _service = review_service

    def find_all_reviews(self):
        return self.find_all()

    def find_review_by_id(self, key):
        return self.find_by_id(key)

    def find_reviews_by_movie_id(self, movie_id):
        return self._service.find_reviews_by_movie_id(movie_id)

    def create_review(self, review):
        return self.create(review)

    def create_all_reviews(self, review_list):
        return self.create_all(review_list)

    def update_review(self, key, new_review):
        return self.update(key, new_review)

    def patch_review(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_review(self, key):
        return self.delete(key)

    def delete_all_reviews(self):
        return self.delete_all()
