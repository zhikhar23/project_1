from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращающая список словарей по ключу"""
    if not transactions:
        return "Пустой список"
    else:
        return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict], ascending: bool = True) -> List[Dict]:
    """Функция для сортировки списка по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=ascending)