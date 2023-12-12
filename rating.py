from __future__ import annotations
from typing import Dict, Any
from app import db


class Rating(db.Model):
    __tablename__ = 'Rating'
    rating_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(45))
    rating_value = db.Column(db.DECIMAL(3,1))
    movie_id = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Rating({self.rating_id}, '{self.user_id}', {self.rating_value}, {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'rating_id': self.rating_id,
            'user_id': self.user_id,
            'rating_value': float(self.rating_value),  # Convert to float for JSON compatibility
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Rating:
        rating = Rating(
            user_id=dto_dict.get('user_id'),
            rating_value=dto_dict.get('rating_value'),
            movie_id=dto_dict.get('movie_id')
        )
        return rating
