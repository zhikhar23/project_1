from typing import Dict, List


def filter_by_state(transactions: List[Dict],
                    state: str = 'EXECUTED') -> List[Dict]:
    """Функция возвращающая список словарей по ключу"""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict]) -> List[Dict]:
    """Функция для сортировки списка по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=True)


#data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# print(filter_by_state(data,state="CANCELED"))
#print(sort_by_date(data))
