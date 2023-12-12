from __future__ import annotations
from typing import Dict, Any
from app import db


class Fact(db.Model):
    __tablename__ = 'Fact'
    fact_id = db.Column(db.Integer, primary_key=True)
    fact_text = db.Column(db.String(255), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Fact({self.fact_id}, '{self.fact_text}', {self.movie_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'fact_id': self.fact_id,
            'fact_text': self.fact_text,
            'movie_id': self.movie_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Fact:
        fact = Fact(
            fact_text=dto_dict.get('fact_text'),
            movie_id=dto_dict.get('movie_id')
        )
        return fact
