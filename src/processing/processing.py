def filter_by_state(transactions, state='EXECUTED'):
    """Filter transactions by state."""
    return [transaction for transaction in transactions if transaction['state'] == state]

def sort_by_date(transactions, reverse=True):
    """Sort transactions by date."""
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)