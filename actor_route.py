from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import actor_controller
from ..domain.actor import Actor

actor_bp = Blueprint('actor', __name__, url_prefix='/actor')


@actor_bp.route('', methods=['GET'])
def get_all_actors() -> Response:
    actors = actor_controller.find_all_actors()
    actor_dtos = [actor.put_into_dto() for actor in actors if isinstance(actor, Actor)]
    return make_response(jsonify(actor_dtos), HTTPStatus.OK)


@actor_bp.route('', methods=['POST'])
def create_actor() -> Response:
    content = request.get_json()
    actor = Actor.create_from_dto(content)
    actor_controller.create_actor(actor)
    return make_response(jsonify(actor.put_into_dto()), HTTPStatus.CREATED)


@actor_bp.route('/<int:actor_id>', methods=['GET'])
def get_actor(actor_id: int) -> Response:
    return make_response(jsonify(actor_controller.find_actor_by_id(actor_id)), HTTPStatus.OK)


@actor_bp.route('/<int:actor_id>', methods=['PUT'])
def update_actor(actor_id: int) -> Response:
    content = request.get_json()
    actor = Actor.create_from_dto(content)
    actor_controller.update_actor(actor_id, actor)
    return make_response("Actor updated", HTTPStatus.OK)


@actor_bp.route('/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id: int) -> Response:
    actor_controller.delete_actor(actor_id)
    return make_response("Actor deleted", HTTPStatus.OK)
