from __future__ import annotations
from typing import Dict, Any
from app import db


class Review(db.Model):
    __tablename__ = 'Review'
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.String(255), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.movie_id'), nullable=False)

    def __repr__(self) -> str:
        return f"Review({self.review_id}, {self.user_id}, '{self.review_text}', {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'review_text': self.review_text,
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        review = Review(
            user_id=dto_dict.get('user_id'),
            review_text=dto_dict.get('review_text'),
            movie_id=dto_dict.get('movie_id')
        )
        return review
