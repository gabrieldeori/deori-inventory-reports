from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from .helpers import Helpers


class Inventory:
    string_simple_report = "simples"
    string_complete_report = "completo"

    @classmethod
    def import_data(cls, path, type):
        list_dict_products = Helpers.resolve_archive(path)

        if type == cls.string_simple_report:
            return SimpleReport.generate(list_dict_products)
        elif type == cls.string_complete_report:
            return CompleteReport.generate(list_dict_products)
