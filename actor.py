from __future__ import annotations
from typing import Dict, Any
from app import db


class Actor(db.Model):
    __tablename__ = 'Actor'
    actor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Actor({self.actor_id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'actor_id': self.actor_id,
            'name': self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actor:
        actor = Actor(
            name=dto_dict.get('name')
        )
        return actor
