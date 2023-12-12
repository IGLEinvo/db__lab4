from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import boxoffice_controller
from ..domain.boxoffice import BoxOffice

boxoffice_bp = Blueprint('boxoffice', __name__, url_prefix='/boxoffice')


@boxoffice_bp.route('', methods=['GET'])
def get_all_boxoffices() -> Response:
    return make_response(jsonify([{'box_office_id': boxoffice['box_office_id'], 'country': boxoffice['country'], 'revenue': boxoffice['revenue'], 'movie_id': boxoffice['movie_id']} for boxoffice in boxoffice_controller.find_all_boxoffices()]), HTTPStatus.OK)


@boxoffice_bp.route('/boxoffice', methods=['POST'])
def create_boxoffice():
    content = request.get_json()

    # Оновлений код: передавайте лише необхідні дані
    boxoffice = BoxOffice.create_from_dto(content)

    boxoffice_controller.create_boxoffice(boxoffice)
    return make_response(jsonify(boxoffice.put_into_dto()), HTTPStatus.CREATED)


@boxoffice_bp.route('/<int:boxoffice_id>', methods=['GET'])
def get_boxoffice(boxoffice_id: int) -> Response:
    return make_response(jsonify(boxoffice_controller.find_boxoffice_by_id(boxoffice_id)), HTTPStatus.OK)


@boxoffice_bp.route('/<int:boxoffice_id>', methods=['PUT'])
def update_boxoffice(boxoffice_id: int) -> Response:
    content = request.get_json()
    boxoffice = BoxOffice.create_from_dto(content)
    boxoffice_controller.update_boxoffice(boxoffice_id, boxoffice)
    return make_response("BoxOffice updated", HTTPStatus.OK)


@boxoffice_bp.route('/<int:boxoffice_id>', methods=['DELETE'])
def delete_boxoffice(boxoffice_id: int) -> Response:
    boxoffice_controller.delete_boxoffice(boxoffice_id)
    return make_response("BoxOffice deleted", HTTPStatus.OK)
