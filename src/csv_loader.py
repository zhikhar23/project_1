import csv
from pprint import pprint


def loader(path: str) -> list[dict]:
    res = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            res.append(row)
    return res


a = loader("../data/titanic.csv")
pprint(a)
