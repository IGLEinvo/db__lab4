# fact_controller.py
from .general_controller import GeneralController
from ..service import fact_service


class FactController(GeneralController):
    _service = fact_service

    def find_all_facts(self):
        return self.find_all()

    def find_fact_by_id(self, key):
        return self.find_by_id(key)

    def create_fact(self, fact):
        return self.create(fact)

    def create_all_facts(self, fact_list):
        return self.create_all(fact_list)

    def update_fact(self, key, new_fact):
        return self.update(key, new_fact)

    def patch_fact(self, key, value_dict):
        return self.patch(key, value_dict)

    def delete_fact(self, key):
        return self.delete(key)

    def delete_all_facts(self):
        return self.delete_all()
