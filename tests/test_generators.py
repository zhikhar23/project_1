from generators import filter_by_currency,transaction_descriptions,card_number_generator
import pytest

@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]

def test_filter(transactions):
    """Функция фильтра по коду транзакции"""
    i=filter_by_currency(transactions,"USD")
    assert next(i)=={
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(i)=={
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }

def test_description(transactions):
    """Функция тестирует вывод по описанию транзакции"""
    i=transaction_descriptions(transactions)
    assert next(i) == "Перевод организации"
    assert next(i)=="Перевод со счета на счет"

def test_generator():
    """Функция тестирует генератор номера карты"""
    expected_result=["0000 0000 0000 0001",
                     "0000 0000 0000 0002",
                     "0000 0000 0000 0003",
                     "0000 0000 0000 0004",
                     "0000 0000 0000 0005"]
    result=list(card_number_generator(1,5))
    assert result==expected_result
