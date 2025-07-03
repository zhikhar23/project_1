import pytest
from src.main import filter_by_description

@pytest.fixture
def json_transactions():
    """Фикстура для json файла"""
    return [
         {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }]

def test_filter_csv_by_description_transfer(json_transactions):
    """Тестирует поиск по слову "перевод"""
    def mock_input(_):
        return "Перевод"

    import builtins
    original_input = builtins.input
    builtins.input = mock_input

    try:
        filtered = filter_by_description("да", json_transactions)
        assert len(filtered) == 5
        assert all("Перевод" in t["description"] for t in filtered)
    finally:
        builtins.input = original_input

def test_filter_csv_by_description_not_found(json_transactions):
    """Проверка по несуществующему описанию"""
    def mock_input(_):
        return "Описание не найдено"

    import builtins
    original_input = builtins.input
    builtins.input = mock_input

    try:
        filtered = filter_by_description("да", json_transactions)
        assert len(filtered) == 0
    finally:
        builtins.input = original_input