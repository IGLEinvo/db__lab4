# boxoffice_dao.py
from .general_dao import GeneralDAO
from ..domain import BoxOffice


class BoxOfficeDAO(GeneralDAO):
    _domain_type = BoxOffice

    def find_all_boxoffices(self):
        return self.find_all()

    def find_boxoffice_by_id(self, boxoffice_id):
        return self.find_by_id(boxoffice_id)

    def find_boxoffice_by_movie_id(self, movie_id):
        return self._session.query(self._domain_type).filter_by(movie_id=movie_id).all()

    def find_boxoffice_by_total_earnings(self, total_earnings):
        return self._session.query(self._domain_type).filter_by(total_earnings=total_earnings).all()

    def create_boxoffice(self, boxoffice):
        return self.create(boxoffice)

    def create_all_boxoffices(self, boxoffice_list):
        return self.create_all(boxoffice_list)

    def update_boxoffice(self, boxoffice_id, updated_boxoffice):
        return self.update(boxoffice_id, updated_boxoffice)

    def patch_boxoffice(self, boxoffice_id, field_name, value):
        return self.patch(boxoffice_id, field_name, value)

    def delete_boxoffice(self, boxoffice_id):
        return self.delete(boxoffice_id)

    def delete_all_boxoffices(self):
        return self.delete_all()
