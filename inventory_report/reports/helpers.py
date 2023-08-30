import statistics
from collections import Counter
from datetime import datetime


class Helpers:
    string_fabrication_date = "data_de_fabricacao"
    string_expiration_date = "data_de_validade"
    string_company_name = "nome_da_empresa"
    template_date_time = "%Y-%m-%d"

    @classmethod
    def get_earliest_manufacture_date(cls, list_dict_products):
        fabrication_date = [
            product[cls.string_fabrication_date]
            for product in list_dict_products
        ]
        fabrication_date.sort()
        earliest_manufacture_date = fabrication_date[0]
        return earliest_manufacture_date

    @classmethod
    def get_closest_expiration_date(cls, list_dict_products):
        current_date = datetime.now().strftime(cls.template_date_time)
        list_expirations_date = []
        for product in list_dict_products:
            expiration_date = product[cls.string_expiration_date]
            if current_date < expiration_date:
                list_expirations_date.append(expiration_date)
        list_expirations_date.sort()
        closest_expiration_date = list_expirations_date[0]
        return closest_expiration_date

    @classmethod
    def get_companies_greatest_stock(cls, list_dict_products):
        companies = [
            product[cls.string_company_name]
            for product in list_dict_products
        ]
        companies_greatest_stock = statistics.multimode(companies)
        return companies_greatest_stock

    @classmethod
    def get_products_stocked_company(cls, list_dict_products):
        companies = [
            product[cls.string_company_name]
            for product in list_dict_products
        ]
        products_stocked_company = Counter(companies)
        return products_stocked_company.items()
