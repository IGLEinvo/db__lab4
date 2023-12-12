# fact_service.py
from .general_service import GeneralService
from ..dao import fact_dao


class FactService(GeneralService):
    _dao = fact_dao

    def find_all_facts(self):
        return self._dao.find_all_facts()

    def find_fact_by_id(self, key):
        return self._dao.find_by_id(key)

    def create_fact(self, fact):
        return self._dao.create(fact)

    def create_all_facts(self, fact_list):
        return self._dao.create_all(fact_list)

    def update_fact(self, key, new_fact):
        return self._dao.update(key, new_fact)

    def patch_fact(self, key, value_dict):
        return self._dao.patch(key, value_dict)

    def delete_fact(self, key):
        return self._dao.delete(key)

    def delete_all_facts(self):
        return self._dao.delete_all()
