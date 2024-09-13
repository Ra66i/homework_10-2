import pytest
from src.widget import get_mask_card_number, get_mask_account


@pytest.fixture
def sample_card_numbers():
    """Возвращает список примеров номеров банковских карт для тестирования"""
    return [
        ('1234567890123456', '************3456'),
        ('1234-5678-9012-3456', '************3456'),
        ('', ''),
        ('1234', '1234'),
    ]


def test_get_mask_card_number(sample_card_numbers):
    """Тестирование функции маскирования номера банковской карты"""
    for input_number, expected_output in sample_card_numbers:
        assert get_mask_card_number(input_number) == expected_output


def test_get_mask_account():
    """Тестирование функции маскирования номера банковского счета"""
    assert get_mask_account('1234567890') == '*****7890'
    assert get_mask_account('') == ''
    assert get_mask_account('1234') == '1234'