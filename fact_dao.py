# fact_dao.py
from .general_dao import GeneralDAO
from ..domain import Fact


class FactDAO(GeneralDAO):
    _domain_type = Fact

    def find_all_facts(self):
        facts = self.find_all()
        print(f"Found facts: {facts}")
        return facts

    def find_fact_by_id(self, fact_id):
        return self.find_by_id(fact_id)

    def create_fact(self, fact):
        return self.create(fact)

    def create_all_facts(self, fact_list):
        return self.create_all(fact_list)

    def update_fact(self, fact_id, updated_fact):
        return self.update(fact_id, updated_fact)

    def patch_fact(self, fact_id, field_name, value):
        return self.patch(fact_id, field_name, value)

    def delete_fact(self, fact_id):
        return self.delete(fact_id)

    def delete_all_facts(self):
        return self.delete_all()
