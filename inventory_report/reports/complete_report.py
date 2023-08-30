from .helpers import Helpers
from .simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(list_dict_products):
        simple_report = SimpleReport.generate(list_dict_products)
        products_stocked_company = Helpers.\
            get_products_stocked_company(list_dict_products)
        complete_report = f"{simple_report}\n" \
                          "Produtos estocados por empresa: \n"

        for company, quantity in products_stocked_company:
            complete_report += f"- {company}: {quantity}\n"

        return complete_report
