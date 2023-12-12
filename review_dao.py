# review_dao.py
from .general_dao import GeneralDAO
from ..domain import Review


class ReviewDAO(GeneralDAO):
    _domain_type = Review

    def find_all_reviews(self):
        reviews = self.find_all()
        print(f"Found reviews: {reviews}")
        return reviews

    def find_reviews_by_movie_id(self, movie_id):
        return self._session.query(self._domain_type).filter_by(movie_id=movie_id).all()

    def find_review_by_id(self, review_id):
        return self.find_by_id(review_id)

    def create_review(self, review):
        return self.create(review)

    def create_all_reviews(self, review_list):
        return self.create_all(review_list)

    def update_review(self, review_id, updated_review):
        return self.update(review_id, updated_review)

    def patch_review(self, review_id, field_name, value):
        return self.patch(review_id, field_name, value)

    def delete_review(self, review_id):
        return self.delete(review_id)

    def delete_all_reviews(self):
        return self.delete_all()
