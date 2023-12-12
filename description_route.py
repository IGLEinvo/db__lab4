from flask import Blueprint, jsonify, request, make_response, Response
from http import HTTPStatus
from ..controller import description_controller
from ..domain import Description

description_bp = Blueprint('description', __name__, url_prefix='/description')


@description_bp.route('', methods=['GET'])
def get_all_descriptions() -> Response:
    descriptions = description_controller.find_all_descriptions()
    print(f"Found objects: {descriptions}")

    # Create Description objects from dictionaries
    description_objects = [Description.create_from_dto(description) for description in descriptions]

    description_dtos = [description.put_into_dto() for description in description_objects if
                        isinstance(description, Description)]
    print(f"Description DTOs: {description_dtos}")

    return make_response(jsonify(description_dtos), HTTPStatus.OK)


@description_bp.route('/<int:description_id>', methods=['GET'])
def get_description(description_id):
    return make_response(jsonify(description_controller.find_description_by_id(description_id)), HTTPStatus.OK)


@description_bp.route('', methods=['POST'])
def create_description():
    content = request.get_json()
    description = description_controller.create_description(content)
    return make_response(jsonify(description.put_into_dto()), HTTPStatus.CREATED)


@description_bp.route('/<int:description_id>', methods=['PUT'])
def update_description(description_id):
    content = request.get_json()
    description_controller.update_description(description_id, content)
    return make_response("Description updated", HTTPStatus.OK)


@description_bp.route('/<int:description_id>', methods=['DELETE'])
def delete_description(description_id):
    description_controller.delete_description(description_id)
    return make_response("Description deleted", HTTPStatus.OK)
