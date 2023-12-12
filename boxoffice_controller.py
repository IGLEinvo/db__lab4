# boxoffice_controller.py
from .general_controller import GeneralController
from ..service import boxoffice_service


class BoxOfficeController(GeneralController):
    _service = boxoffice_service

    def find_all_boxoffices(self):
        return self.find_all()

    def find_boxoffice_by_id(self, key):
        return self.find_by_id(key)

    def create_boxoffice(self, boxoffice):
        return self.create(boxoffice)

    def create_all_boxoffices(self, boxoffice_list):
        return self.create_all(boxoffice_list)

    def update_boxoffice(self, key, new_boxoffice):
        return self.update(key, new_boxoffice)

    def patch_boxoffice(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_boxoffice(self, key):
        return self.delete(key)

    def delete_all_boxoffices(self):
        return self.delete_all()
