
class ElectricityUsageModel:
    def __init__(self, product_id, product_name, price_per_hour, consumption_per_hour, avr_daily_usage):
        self.__id = product_id
        self.__name = product_name
        self.__price = price_per_hour
        self.__consumption = consumption_per_hour
        self.__usage = avr_daily_usage

    def get_product_id(self):
        return self.__id

    def set_product_id(self, product_id):
        if type(product_id) == int:
            self.__id = product_id


    def get_product_name(self):
        return self.__name

    def set_product_name(self, product_name):
        if type(product_name) == str:
            self.__name = product_name


    def get_price_per_hour(self):
        return self.__price

    def set_price_per_hour(self, price_per_hour):
        if type(price_per_hour) == float:
            self.__price = price_per_hour


    def get_consumption_per_hour(self):
        return self.__consumption

    def set_consumption_per_hour(self, consumption_per_hour):
        if type(consumption_per_hour) == float:
            self.__consumption = consumption_per_hour


    def get_avr_daily_usage(self):
        return self.__usage

    def set_avr_daily_usage(self, avr_daily_usage):
        if type(avr_daily_usage) == float:
            self.__usage = avr_daily_usage

