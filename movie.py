from __future__ import annotations
from typing import Dict, Any
from app import db


class Movie(db.Model):
    __tablename__ = 'Movie'
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    release_date = db.Column(db.String(45), nullable=False)
    genre = db.Column(db.String(45), nullable=False)
    director = db.Column(db.String(45), nullable=False)
    runtime = db.Column(db.String(45), nullable=False)

    # Add this line for the reverse relationship
    description = db.relationship('Description', back_populates='movie')

    def __repr__(self) -> str:
        return f"Movie({self.movie_id}, '{self.title}', '{self.release_date}', '{self.genre}', '{self.director}', '{self.runtime}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'release_date': self.release_date,
            'genre': self.genre,
            'director': self.director,
            'runtime': self.runtime
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Movie:
        movie = Movie(
            title=dto_dict.get('title'),
            release_date=dto_dict.get('release_date'),
            genre=dto_dict.get('genre'),
            director=dto_dict.get('director'),
            runtime=dto_dict.get('runtime')
        )
        return movie
