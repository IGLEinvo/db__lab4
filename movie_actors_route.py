# movieactors_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import movie_actors_controller
from ..domain.movie_actors import MovieActors

movie_actors_bp = Blueprint('movieactors', __name__, url_prefix='/movieactors')


@movie_actors_bp.route('', methods=['GET'])
def get_all_movie_actors() -> Response:
    movie_actors = movie_actors_controller.find_all_movie_actors()
    movie_actors_dtos = [movie_actor.put_into_dto() for movie_actor in movie_actors if isinstance(movie_actor, MovieActors)]
    return make_response(jsonify(movie_actors_dtos), HTTPStatus.OK)


@movie_actors_bp.route('/<int:actor_id>/<int:movie_id>', methods=['GET'])
def get_movie_actor(actor_id: int, movie_id: int) -> Response:
    return make_response(jsonify(movie_actors_controller.find_movie_actor_by_ids(actor_id, movie_id)), HTTPStatus.OK)


@movie_actors_bp.route('', methods=['POST'])
def create_movie_actor() -> Response:
    content = request.get_json()
    movie_actor = MovieActors.create_from_dto(content)
    movie_actors_controller.create_movie_actor(movie_actor)
    return make_response(jsonify(movie_actor.put_into_dto()), HTTPStatus.CREATED)


@movie_actors_bp.route('', methods=['PUT'])
def update_movie_actor() -> Response:
    content = request.get_json()
    actor_id = content.get('actor_id')
    movie_id = content.get('movie_id')
    movie_actor = MovieActors.create_from_dto(content)
    movie_actors_controller.update_movie_actor(actor_id, movie_id, movie_actor)
    return make_response("Movie actor updated", HTTPStatus.OK)


@movie_actors_bp.route('/<int:actor_id>/<int:movie_id>', methods=['DELETE'])
def delete_movie_actor(actor_id: int, movie_id: int) -> Response:
    movie_actors_controller.delete_movie_actor(actor_id, movie_id)
    return make_response("Movie actor deleted", HTTPStatus.OK)
