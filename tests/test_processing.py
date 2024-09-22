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

@pytest.mark.parametrize("state, expected_length, expected_ids", [
    ('EXECUTED', 2, [1, 3]),
    ('PENDING', 1, [2]),
    ('CANCELED', 0, []),
])
def filter_by_state(transactions, state):
    filtered = []
    for transaction in transactions:
        if transaction['state'] == state:
            filtered.append(transaction)
    return filtered if filtered else []

@pytest.mark.parametrize("expected_ids", [
    ([3, 2, 1]),  # Сортировка по дате в обратном порядке
    ([1, 2, 3]),  # Сортировка по дате в прямом порядке
])

def sort_by_date(transactions, reverse=True):
    """
    Сортировка транзакций по дате.

    Параметры:
    transactions (list): Список транзакций для сортировки.
    reverse (bool, optional): Если True, сортировка в порядке убывания. По умолчанию True.

    Возвращает:
    list: Отсортированный список транзакций по дате.
    """
    if not transactions:
        return []
    sorted_transactions = sorted(transactions, key=lambda t: t['date'], reverse=reverse)
    return sorted_transactions

@pytest.mark.parametrize("expected_ids, reverse", [
    ([3, 2, 1], True),  # Сортировка по дате в обратном порядке
    ([1, 2, 3], False),  # Сортировка по дате в прямом порядке
])
def test_sort_by_date(sample_transactions, expected_ids, reverse):
    """Тестирование функции сортировки транзакций по дате с параметризацией"""
    sorted_transactions = sort_by_date(sample_transactions, reverse=reverse)
    if sorted_transactions:
        assert [t['id'] for t in sorted_transactions] == expected_ids
    else:
        assert sorted_transactions == []