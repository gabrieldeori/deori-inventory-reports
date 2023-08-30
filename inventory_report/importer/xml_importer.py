import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path, 'r') as file:
                raw_products = xmltodict.parse(file.read())
                list_dict_products = [  # Mesmo de helpers de inventory
                    dict(product)
                    for product in raw_products["dataset"]["record"]
                ]
                return list_dict_products
        raise ValueError("Arquivo inválido")

# Não importei as funções pq é interessante manter a distinção da arquitetura
# "antiga" com essa "nova". Além do que são "contextos" distintos.
