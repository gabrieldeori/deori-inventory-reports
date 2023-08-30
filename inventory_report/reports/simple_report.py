from .helpers import Helpers


class SimpleReport:
    @staticmethod
    def generate(list_dict_products):
        earliest_manufacture_date = \
            Helpers.get_earliest_manufacture_date(list_dict_products)
        closest_expiration_date = \
            Helpers.get_closest_expiration_date(list_dict_products)
        companies_greatest_stock = \
            Helpers.get_companies_greatest_stock(list_dict_products)

        report = "Data de fabricação mais antiga: " \
                 f"{earliest_manufacture_date}\n" \
                 "Data de validade mais próxima: " \
                 f"{closest_expiration_date}\n"

        if len(companies_greatest_stock) > 1:
            report += "Empresas com maiores quantidades " \
                      "de produtos estocados:\n"
            for company in companies_greatest_stock:
                print(f" - {company}")
        elif len(companies_greatest_stock) == 1:
            company_greatest_stock = companies_greatest_stock[0]
            report += "Empresa com maior quantidade de produtos " \
                      f"estocados: {company_greatest_stock}\n"

        return report
