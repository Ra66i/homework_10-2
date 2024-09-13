from datetime import datetime

def mask_account_card(info: str) -> str:
    """
    Маскирует номер банковского счета или карты.

    Если строка начинается с "Счет", маскируется номер счета,
    отображая только последние 4 цифры. В противном случае
    маскируется номер карты, отображая первые 6 и последние 4 цифры.

    Args:
        info (str): Строка, содержащая либо номер счета, либо номер карты.

    Returns:
        str: Маскированная строка с номером счета или карты.
    """
    if info.startswith("Счет"):
        # Маскировка счета
        return f"Счет **{info[-4:]}"
    else:
        # Маскировка карты
        parts = info.split()
        card_number = parts[-1]
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return " ".join(parts[:-1]) + " " + masked_number

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_str (str): Дата в формате ISO (ГГГГ-ММ-ДД).

    Returns:
        str: Дата в формате ДД.ММ.ГГГГ.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
