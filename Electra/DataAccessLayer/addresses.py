from Electra.DataAccessLayer.connection import *
from Electra.BusinessLayer.addresses_model import *


class Addresses:
    def __init__(self):
        self.connect = Connection()
        self.connection = self.connect.connection


    def read_all_addresses(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Addresses')
        data = cursor.fetchall()
        address_list = []
        for row in data:
            address = AddressModel(address_id=row[0], region=row[1], city=row[2], user_id=row[3])
            address_list.append(address)
        return address_list

    def create_address(self,address):
        cursor = self.connection.cursor()
        query = "Insert into Addresses (address_id, region, city, user_id) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (address.get_id(), address.get_region(), address.get_city(), address.get_user_id()))
        self.connection.commit()

    def update_address(self,address):
        cursor = self.connection.cursor()
        cursor.execute("Update Addresses set region = ? where address_id = ?", (address.get_region(), address.get_id()))
        cursor.execute("Update Addresses set city = ? where address_id = ?", (address.get_city(), address.get_id()))
        self.connection.commit()

    def delete_address(self,address):
        cursor = self.connection.cursor()
        query = "Delete from Addresses where address_id = ?"
        cursor.execute(query, address.get_id())
        self.connection.commit()

