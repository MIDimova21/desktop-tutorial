from Electra.DataAccessLayer.connection import *
from Electra.BusinessLayer.electricity_model import *


class ElectricityUsage:
    def __init__(self):
        self.connect = Connection()
        self.connection = self.connect.connection


    def read_all_electricity_usages(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Electricity_Usage')
        data = cursor.fetchall()
        electricity_list = []
        for row in data:
            electricity = ElectricityUsageModel(product_id=row[0], product_name=row[1], price_per_hour=row[2], consumption_per_hour=row[3], avr_daily_usage=row[4])
            electricity_list.append(row)
        return electricity_list

    def read_electricity_usage_by_id(self, id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Electricity_Usage')
        data = cursor.fetchall()
        all = []
        for row in data:
            if row[0] in id:
                all.append(row)
        return all

    def add_electricity_usage(self,electricity):
        cursor = self.connection.cursor()
        query = "Insert into Electricity_Usage (electricity_id, product_name, price_per_hour, consumption_per_hour, avr_daily_usage) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (electricity.get_product_id(), electricity.get_product_name(), electricity.get_price_per_hour(), electricity.get_consumption_per_hour(), electricity.get_avr_daily_usage()))
        self.connection.commit()

    def update_electricity_usage(self,electricity):
        cursor = self.connection.cursor()
        cursor.execute("Update Electricity_Usage set consumption_per_hour = ? where electricity_id = ?", (electricity.get_consumption_per_hour(), electricity.get_id()))
        cursor.execute("Update Electricity_Usage set price_per_hour = ? where electricity_id = ?", (electricity.get_price_per_hour(), electricity.get_id()))
        self.connection.commit()

    def delete_electricity_usage(self,electricity):
        cursor = self.connection.cursor()
        query = "Delete from Electricity_Usage where electricity_id = ?"
        cursor.execute(query, electricity.get_id())
        self.connection.commit()





