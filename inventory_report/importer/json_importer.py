import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path, 'r') as file:
                with open(path, 'r') as file:
                    list_dict_products = json.load(file)
                    return list_dict_products
        raise ValueError("Arquivo inválido")
