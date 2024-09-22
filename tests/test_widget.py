import pytest
from src.widget.widget import mask_account_card

@pytest.mark.parametrize("input_string, expected_output", [
    ('1234567890123456', '************3456'),
    ('1234567890', '*****7890'),
    ('', ''),
    ('1234', '1234'),
])
def mask_account_card(card_number: str) -> str:
    """
    Тестирование функции mask_account_card с параметризацией.

    Параметры:
    input_string (str): Входная строка для маскирования.
    expected_output (str): Ожидаемый результат после маскирования.

    Возвращает:
    None

    """
    return f"{card_number[:4]} {card_number[4:8]}** **** {card_number[12:]}"