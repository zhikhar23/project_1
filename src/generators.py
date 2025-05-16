from typing import Generator, Any


def filter_by_currency(transactions:list[dict[str,Any]], currency:str)->Generator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transaction_list: list) -> Generator[str]:
    for i in transaction_list:
        if i.get("description"):
            yield i["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        card_number = start_card_number[: -len(str(num))] + str(num)
        if len(card_number) > 16:
            raise ValueError("Неверный номер карты")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
