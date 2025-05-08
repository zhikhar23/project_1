from  src.processing import filter_by_state , sort_by_date
import pytest

@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]

def test_filter_by_state(transactions):
    """Фунцкия для тестирования при помощи фикстур"""
    assert filter_by_state(transactions, state = 'EXECUTED') == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
def test_filter_by_state1(transactions):
    assert filter_by_state(transactions, state = 'CANCELED') == [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
def test_filter_by_state_empty(transactions):
    assert filter_by_state([])=="Пустой список"
def test_filter_by_state3(transactions):
    assert filter_by_state(transactions)==[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
def test_filter_by_state4(transactions):
    assert filter_by_state(transactions, state ='None')==[]

def test_date(transactions):
    """Функия для проверки сортировки с использованием фикстуры"""
    assert sort_by_date(transactions)==[{'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
 {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
 {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
 {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}]
def test_date1(transactions):
    """Функия для проверки сортировки в обратном порядке с использованием фикстуры """
    assert sort_by_date(transactions,ascending=False)==[{'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
 {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
 {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
 {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'}]
def test_date2(transactions):
    assert sort_by_date([])==[]
