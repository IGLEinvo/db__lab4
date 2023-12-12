from .general_dao import GeneralDAO
from ..domain import Description


class DescriptionDAO(GeneralDAO):
    _domain_type = Description

    def find_all_descriptions(self):
        descriptions = self.find_all()
        return descriptions

    def find_description_by_id(self, description_id):
        return self.find_by_id(description_id)

    def create_description(self, description):
        return self.create(description)

    def update_description(self, description_id, updated_description):
        return self.update(description_id, updated_description)

    def delete_description(self, description_id):
        return self.delete(description_id)
