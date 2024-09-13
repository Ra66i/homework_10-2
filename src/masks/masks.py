# src/masks/masks.py


def get_mask_card_number(card_number: int) -> str:
    """Returns masked bank card number.

    Format: XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    masked = card_str[:4] + " " + card_str[4:6] + "** **** " + card_str[-4:]
    return masked


def get_mask_account(account_number: int) -> str:
    """Returns masked bank account number.

    Format: **XXXX
    """
    account_str = str(account_number)
    masked = "**" + account_str[-4:]
    return masked
