import pytest
from src.masks.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def sample_card_numbers():
    """Возвращает список примеров номеров банковских карт для тестирования"""
    return [
        ('1234567890123456', '************3456'),
        ('1234-5678-9012-3456', '************3456'),
        ('', ''),
        ('1234', '1234'),
    ]

@pytest.mark.parametrize("input_number, expected_output", [
    ('1234567890123456', '************3456'),
    ('1234-5678-9012-3456', '************3456'),
    ('', ''),
    ('1234', '1234'),
])
def get_mask_card_number(card_number: str) -> str:
    return f"{card_number[:12]}****{card_number[-4:]}"

def get_mask_account(account: str) -> str:
    return f"**{account[2:]}"