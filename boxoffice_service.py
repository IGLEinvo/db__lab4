# boxoffice_service.py
from .general_service import GeneralService
from ..dao import boxoffice_dao


class BoxOfficeService(GeneralService):
    _dao = boxoffice_dao

    def find_all_boxoffice(self):
        return self._dao.find_all_boxoffice()

    def find_boxoffice_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_boxoffice(self, boxoffice):
        return self._dao.create(boxoffice)

    def create_all_boxoffice(self, boxoffice_list):
        return self._dao.create_all(boxoffice_list)

    def update_boxoffice(self, key, new_boxoffice):
        return self._dao.update(key, new_boxoffice)

    def patch_boxoffice(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_boxoffice(self, key):
        return self._dao.delete(key)

    def delete_all_boxoffice(self):
        return self._dao.delete_all()
