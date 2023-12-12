# movie_actors.py
from __future__ import annotations
from typing import Dict, Any
from app import db


class MovieActors(db.Model):
    __tablename__ = 'MovieActors'
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.actor_id'), primary_key=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.movie_id'), primary_key=True, nullable=False)

    def __repr__(self) -> str:
        return f"MovieActors({self.actor_id}, {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'actor_id': self.actor_id,
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MovieActors:
        movie_actors = MovieActors(
            actor_id=dto_dict.get('actor_id'),
            movie_id=dto_dict.get('movie_id')
        )
        return movie_actors
