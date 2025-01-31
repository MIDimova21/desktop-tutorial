from Electra.DataAccessLayer.addresses import Addresses
from Electra.BusinessLayer.addresses_model import AddressModel


class AddressesService:

    def get_all_addresses(self):
        address = Addresses()
        addresses_list = [address.read_all_addresses()]
        for row in addresses_list:
            model = AddressModel(address_id=row[0], region=row[1], city=row[2], user_id=row[3])
        return addresses_list

    def update_address(self, model):
        address = Addresses()
        addresses = address.update_address(model)
        return addresses

    def add_address(self, model):
        address = Addresses()
        address.create_address(model)

    def delete_address(self, model):
        address = Addresses()
        address.delete_address(model)

