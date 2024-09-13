# tests/test_widget.py

import pytest
from src.widget.widget import mask_account_card

def test_mask_account_card():
    """
    Тестирование функции mask_account_card.

    Функция должна заменить все символы в входной строке, кроме последних 4, на звездочки (*).
    Если входная строка короче 4 символов, она должна быть возвращена без изменений.

    Параметры:
    Нет

    Возвращает:
    Нет

    """
    assert mask_account_card('1234567890123456') == '************3456'
    assert mask_account_card('1234567890') == '*****7890'
    assert mask_account_card('') == ''
    assert mask_account_card('1234') == '1234'