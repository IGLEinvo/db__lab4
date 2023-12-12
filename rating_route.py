from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import rating_controller
from ..domain.rating import Rating

rating_bp = Blueprint('rating', __name__, url_prefix='/rating')


@rating_bp.route('', methods=['GET'])
def get_all_ratings() -> Response:
    ratings = rating_controller.find_all_ratings()
    rating_dtos = [rating.put_into_dto() for rating in ratings if isinstance(rating, Rating)]
    return make_response(jsonify(rating_dtos), HTTPStatus.OK)


@rating_bp.route('', methods=['POST'])
def create_rating() -> Response:
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    rating_controller.create_rating(rating)
    return make_response(jsonify(rating.put_into_dto()), HTTPStatus.CREATED)


@rating_bp.route('/<int:rating_id>', methods=['GET'])
def get_rating(rating_id: int) -> Response:
    return make_response(jsonify(rating_controller.find_rating_by_id(rating_id)), HTTPStatus.OK)


@rating_bp.route('/<int:rating_id>', methods=['PUT'])
def update_rating(rating_id: int) -> Response:
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    rating_controller.update_rating(rating_id, rating)
    return make_response("Rating updated", HTTPStatus.OK)


@rating_bp.route('/<int:rating_id>', methods=['DELETE'])
def delete_rating(rating_id: int) -> Response:
    rating_controller.delete_rating(rating_id)
    return make_response("Rating deleted", HTTPStatus.OK)
