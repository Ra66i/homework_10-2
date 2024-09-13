def get_mask_card_number(card_number: int) -> str:
    """Возвращает маскированный номер банковской карты.

    Формат: XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    masked = card_str[:4] + " " + card_str[4:6] + "** **** " + card_str[-4:]
    return masked


def get_mask_account(account_number: int) -> str:
    """Возвращает маскированный номер банковского счета.

    Формат: **XXXX
    """
    account_str = str(account_number)
    masked = "**" + account_str[-4:]
    return masked