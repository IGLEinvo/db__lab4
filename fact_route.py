# fact_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import fact_controller
from ..domain.fact import Fact

fact_bp = Blueprint('fact', __name__, url_prefix='/fact')


@fact_bp.route('', methods=['GET'])
def get_all_facts() -> Response:
    facts = fact_controller.find_all_facts()
    fact_dtos = [fact.put_into_dto() for fact in facts if isinstance(fact, Fact)]
    return make_response(jsonify(fact_dtos), HTTPStatus.OK)


@fact_bp.route('', methods=['POST'])
def create_fact() -> Response:
    content = request.get_json()
    fact = Fact.create_from_dto(content)
    fact_controller.create_fact(fact)
    return make_response(jsonify(fact.put_into_dto()), HTTPStatus.CREATED)


@fact_bp.route('/<int:fact_id>', methods=['GET'])
def get_fact(fact_id: int) -> Response:
    return make_response(jsonify(fact_controller.find_fact_by_id(fact_id)), HTTPStatus.OK)


@fact_bp.route('/<int:fact_id>', methods=['PUT'])
def update_fact(fact_id: int) -> Response:
    content = request.get_json()
    fact = Fact.create_from_dto(content)
    fact_controller.update_fact(fact_id, fact)
    return make_response("Fact updated", HTTPStatus.OK)


@fact_bp.route('/<int:fact_id>', methods=['DELETE'])
def delete_fact(fact_id: int) -> Response:
    fact_controller.delete_fact(fact_id)
    return make_response("Fact deleted", HTTPStatus.OK)
