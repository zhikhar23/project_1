import json
import os

import pytest

from src.external_api import transaction_summ
from unittest.mock import Mock
from unittest.mock import patch
import json
from src.utils import get_transactions
import pytest
import requests

def test_get_transaction():
    """Тестируем функция с помощью Моск"""
    mock_2=Mock(return_value=[{'d':3},{"d":3}])
    json.load=mock_2
    assert get_transactions(json_path="../data/operations.json")==[{'d':3},{"d":3}]
    mock_2.assert_called_once()

@pytest.fixture
def transact_list():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "1",
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
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }
]
@patch('requests.get')
def test_transact_summ(mock_get,transact_list):
    """Тестируем с помощью patch"""
    mock_response=mock_get.return_value
    mock_response.status_code=200
    mock_response.json.return_value = {"result":1}
    assert transaction_summ(transact_list,"RUB")==2