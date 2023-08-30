import csv
import json
import xmltodict
# Pesquisei no slack de todas as turmas, vi o pessoal usando o xmltodict desde
# a T6. PS: Todos tiveram o mesmo problema com dev-requirements.txt :D
# https://www.geeksforgeeks.org/python-program-to-convert-xml-to-dictionary/
# Primeira opção: pip install xmltodict


class Helpers:
    @staticmethod
    def read_csv(file):
        raw_products = csv.DictReader(file, delimiter=",", quotechar='"')
        list_dict_products = list(raw_products)
        return list_dict_products

    @staticmethod
    def read_json(file):
        list_dict_products = json.load(file)
        return list_dict_products

    @staticmethod
    def read_xml(file):
        raw_products = xmltodict.parse(file.read())
        list_dict_products = [
            dict(product)  # Converte produto em dict antes de inserir na lista
            for product in raw_products["dataset"]["record"]
            # basta dar print() em raw_products que é possível ver essa struct
        ]
        return list_dict_products

    @classmethod
    def resolve_archive(cls, path):
        with open(path, 'r') as file:
            if path.endswith(".csv"):
                return cls.read_csv(file)
            elif path.endswith(".json"):
                return cls.read_json(file)
            elif path.endswith("xml"):
                return cls.read_xml(file)
