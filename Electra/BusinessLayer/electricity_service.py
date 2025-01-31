from Electra.DataAccessLayer.electricity_usage import ElectricityUsage
from Electra.BusinessLayer.electricity_model import ElectricityUsageModel

class ElectricityUsageService:

    def get_all_electricity_usage(self):
        electricity = ElectricityUsage()
        electricity_list = [electricity.read_all_electricity_usages()]
        return electricity_list

    def get_electricity_usage_by_id(self, id):
        electricity = ElectricityUsage()
        return electricity.read_electricity_usage_by_id(id)

    def update_electricity_usage(self, model):
        electricity = ElectricityUsage()
        electricity_usage = electricity.update_electricity_usage(model)
        return electricity_usage

    def add_electricity_usage(self, model):
        electricity = ElectricityUsage()
        electricity.add_electricity_usage(model)

    def delete_electricity_usage(self, model):
        electricity = ElectricityUsage()
        electricity.delete_electricity_usage(model)

