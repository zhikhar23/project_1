import csv


def loader(path: str) -> list[dict]:
    """7.Добавлены функции для обработки файлов формата csv"""
    res = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            res.append(row)
    return res
