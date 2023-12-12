from __future__ import annotations
from typing import Dict, Any
from app import db


class Description(db.Model):
    __tablename__ = 'Description'
    description_id = db.Column(db.Integer, primary_key=True)
    plot = db.Column(db.TEXT)
    tagline = db.Column(db.TEXT)
    poster_url = db.Column(db.String(255))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.movie_id'), nullable=False)
    movie = db.relationship('Movie', back_populates='description')

    def __repr__(self) -> str:
        return f"Description({self.description_id}, '{self.plot}', '{self.tagline}', '{self.poster_url}', {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'description_id': self.description_id,
            'plot': self.plot,
            'tagline': self.tagline,
            'poster_url': self.poster_url,
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Description:
        description = Description(
            plot=dto_dict.get('plot'),
            tagline=dto_dict.get('tagline'),
            poster_url=dto_dict.get('poster_url'),
            movie_id=dto_dict.get('movie_id')
        )
        return description
