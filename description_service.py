from ..dao import description_dao
from .general_service import GeneralService


class DescriptionService(GeneralService):
    _dao = description_dao

    def find_all_descriptions(self):
        return self._dao.find_all_descriptions()

    def find_description_by_id(self, description_id):
        return self._dao.find_description_by_id(description_id)

    def create_description(self, description):
        return self._dao.create_description(description)

    def update_description(self, description_id, new_description):
        return self._dao.update_description(description_id, new_description)

    def delete_description(self, description_id):
        return self._dao.delete_description(description_id)
