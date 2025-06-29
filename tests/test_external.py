import builtins
import json
import os
import pytest
from src.external_api_2 import transaction_summ
from unittest.mock import Mock, mock_open
from unittest.mock import patch
import json
from src.utils import get_transactions
import pytest
import requests



def test_get_transaction():
    """Тестируем функция с помощью Моск"""
    test_data = [{"id": 1, "amount": 100}]

    os.path.exists = Mock(return_value=True)
    builtins.open = mock_open(read_data=json.dumps(test_data))

    result = get_transactions(" ")
    assert result == test_data
    builtins.open.assert_called_once()

@pytest.fixture
def transaction():
    return {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "дол.",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

@patch('requests.get')
def test_transact_summ(mock_get,transaction):
    """Тестируем с помощью patch"""
    mock_response=mock_get.return_value
    mock_response.status_code=200
    mock_response.json.return_value = {"result":2}
    assert transaction_summ(transaction,"RUB")==2
