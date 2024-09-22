def filter_by_state(transactions, state='EXECUTED'):
    """
    Фильтрация транзакций по состоянию.

    Параметры:
    transactions (list): Список транзакций для фильтрации.
    state (str, optional): Состояние для фильтрации. По умолчанию 'EXECUTED'.

    Возвращает:
    list: Список транзакций, соответствующих указанному состоянию.
    """
    filtered = []
    for transaction in transactions:
        if transaction['state'] == state:
            filtered.append(transaction)
    return filtered if filtered else []

def sort_by_date(transactions, reverse=True):
    """
    Сортировка транзакций по дате.

    Параметры:
    transactions (list): Список транзакций для сортировки.
    reverse (bool, optional): Если True, сортировка в порядке убывания. По умолчанию True.

    Возвращает:
    list: Отсортированный список транзакций по дате.
    """
    if not transactions:
        return []
    sorted_transactions = sorted(transactions, key=lambda t: t['date'], reverse=reverse)
    return sorted_transactions