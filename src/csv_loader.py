import csv
from pprint import pprint


def loader(path: str) -> list[dict]:
    """Функция обработки данных из файла формата csv"""
    res = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            res.append(row)
    return res
