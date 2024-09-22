import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    """Возвращает фикстуру с данными для теста"""
    return [
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
        # Добавьте другие транзакции, если необходимо
    ]

@pytest.mark.parametrize("currency, expected_result", [
    ("USD", [
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
    ]),
    # Добавьте другие примеры, если необходимо
])
def test_filter_by_currency(transactions, currency, expected_result):
    # Проверяет работу функции filter_by_currency с параметризацией валюты
    assert list(filter_by_currency(transactions, currency)) == expected_result


from typing import List, Dict
Transaction = Dict[str, str]

def filter_by_currency(transactions: List[Transaction], currency: str) -> List[Transaction]:
    filtered_transactions = []
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            filtered_transactions.append(transaction)
    return filtered_transactions

def test_transaction_descriptions(transactions):
    # Проверяет работу функции transaction_descriptions
    assert list(transaction_descriptions(transactions)) == [...]

@pytest.mark.parametrize("start, stop, expected_result", [
    (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),  # Пример 1: Диапазон от 1 до 5
    (10, 20, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012", "0000 0000 0000 0013", "0000 0000 0000 0014", "0000 0000 0000 0015", "0000 0000 0000 0016", "0000 0000 0000 0017", "0000 0000 0000 0018", "0000 0000 0000 0019"]),  # Пример 2: Диапазон от 10 до 20
    # Добавьте другие примеры, если необходимо
])
def card_number_generator(start: int, stop: int) -> List[str]:
    for i in range(start, stop + 1):
        card_number = '{:016d}'.format(i)
        card_number = ' '.join([card_number[j:j + 4] for j in range(0, 16, 4)])
        yield card_number


@pytest.mark.parametrize("transactions, expected_result", [
    (
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2022-01-01T00:00:00.000000",
                "operationAmount": {
                    "amount": "100.00",
                    "currency": {
                        "name": "RUB",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 1234567890123456",
                "to": "Счет 12345678901234567890"
            },
            {
                "id": 2,
                "state": "EXECUTED",
                "date": "2022-01-02T00:00:00.000000",
                "operationAmount": {
                    "amount": "200.00",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 98765432109876543210",
                "to": "Счет 11111111111111111111"
            }
        ],
        [
            "Перевод организации",
            "Перевод со счета на счет"
        ]
    ),
    # Добавьте другие примеры, если необходимо
])
def test_transaction_descriptions(transactions, expected_result):
    # Проверяет работу функции transaction_descriptions
    assert list(transaction_descriptions(transactions)) == expected_result


from typing import List, Dict

Transaction = Dict[str, str]

def transaction_descriptions(transactions: List[Transaction]) -> List[str]:
    descriptions = []
    for transaction in transactions:
        descriptions.append(transaction['description'])
    return descriptions