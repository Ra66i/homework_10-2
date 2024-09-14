from typing import List, Dict, Iterator

def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


from typing import List, Dict, Iterator

def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    for transaction in transactions:
        description = transaction["description"]
        if "счет" in description:
            description = "Перевод со счета на счет"
        elif "карта" in description:
            description = "Перевод с карты на карту"
        else:
            description = "Перевод организации"
        yield description

from typing import Iterator

def card_number_generator(start: int, end: int) -> Iterator[str]:
    for number in range(start, end + 1):
        yield f"{number:016d}".replace(" ", "X")