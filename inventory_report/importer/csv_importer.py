import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):  # Flertei com o paradigma.
            with open(path, 'r') as file:
                raw_products = \
                    csv.DictReader(file, delimiter=",", quotechar='"')

                list_dict_products = list(raw_products)
                return list_dict_products
        raise ValueError("Arquivo inválido")
