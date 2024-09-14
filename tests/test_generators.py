import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    # Возвращает фикстуру с данными для теста
    return [...]

def test_filter_by_currency(transactions):
    # Проверяет работу функции filter_by_currency
    assert list(filter_by_currency(transactions, "USD")) == [...]

def test_transaction_descriptions(transactions):
    # Проверяет работу функции transaction_descriptions
    assert list(transaction_descriptions(transactions)) == [...]

def test_card_number_generator():
    # Проверяет работу генератора card_number_generator
    assert list(card_number_generator(1, 5)) == ["XXXX XXXX XXXX XXXX", "XXXX XXXX XXXX XXXX", "XXXX XXXX XXXX XXXX", "XXXX XXXX XXXX XXXX", "XXXX XXXX XXXX XXXX"]