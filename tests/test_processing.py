# tests/test_processing.py

import pytest
from src.processing.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    """Возвращает список примеров транзакций для тестирования"""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
    ]


def test_filter_by_state(sample_transactions):
    """Тестирование функции фильтрации транзакций по состоянию"""
    filtered = filter_by_state(sample_transactions, state='EXECUTED')
    assert len(filtered) == 2
    assert filtered[0]['id'] == 1
    assert filtered[1]['id'] == 3


def test_sort_by_date(sample_transactions):
    """Тестирование функции сортировки транзакций по дате"""
    sorted_transactions = sort_by_date(sample_transactions)
    assert sorted_transactions[0]['id'] == 3
    assert sorted_transactions[-1]['id'] == 1