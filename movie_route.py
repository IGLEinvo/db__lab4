from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import movie_controller, review_controller
from ..domain import Movie, Review

movie_bp = Blueprint('movie', __name__, url_prefix='/movie')


@movie_bp.route('', methods=['GET'])
def get_all_movies() -> Response:
    movies = movie_controller.find_all_movies()
    print(f"Movies found: {movies}")

    movie_dtos = [movie.put_into_dto() for movie in movies if isinstance(movie, Movie)]
    print(f"Movie DTOs: {movie_dtos}")

    return make_response(jsonify(movie_dtos), HTTPStatus.OK)


@movie_bp.route('', methods=['POST'])
def create_movie() -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    movie_controller.create_movie(movie)
    return make_response(jsonify(movie.put_into_dto()), HTTPStatus.CREATED)


@movie_bp.route('/<int:movie_id>', methods=['GET'])
def get_movie(movie_id: int) -> Response:
    return make_response(jsonify(movie_controller.find_movie_by_id(movie_id)), HTTPStatus.OK)


@movie_bp.route('/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id: int) -> Response:
    content = request.get_json()
    movie = Movie.create_from_dto(content)
    movie_controller.update_movie(movie_id, movie)
    return make_response("Movie updated", HTTPStatus.OK)


@movie_bp.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id: int) -> Response:
    movie_controller.delete_movie(movie_id)
    return make_response("Movie deleted", HTTPStatus.OK)


@movie_bp.route('/<int:movie_id>/review', methods=['GET'])
def get_movie_reviews(movie_id: int) -> Response:
    reviews = review_controller.find_reviews_by_movie_id(movie_id)
    review_dtos = [review.put_into_dto() for review in reviews if isinstance(review, Review)]
    return make_response(jsonify(review_dtos), HTTPStatus.OK)
