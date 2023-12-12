from ..service import description_service
from .general_controller import GeneralController


class DescriptionController(GeneralController):
    _service = description_service

    def find_all_descriptions(self):
        return self.find_all()

    def find_description_by_id(self, description_id):
        return self.find_by_id(description_id)

    def create_description(self, description):
        return self.create(description)

    def update_description(self, description_id, new_description):
        return self.update(description_id, new_description)

    def delete_description(self, description_id):
        return self.delete(description_id)
