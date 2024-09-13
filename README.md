# Банковский виджет операций клиента

## Описание

Этот проект разрабатывается для отображения последних банковских операций клиента в его личном кабинете.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Ra66i/homework_10-2.git
cd project-folder

Использование
Функция filter_by_state
Функция принимает список словарей transactions и параметр state (по умолчанию 'EXECUTED'). Возвращает новый список словарей, содержащий только те операции, у которых ключ state равен переданному значению.

python
Copy code
from src.processing.processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]

filtered_transactions = filter_by_state(transactions, state='EXECUTED')
print(filtered_transactions)
# [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}]
Функция sort_by_date
Функция принимает список словарей transactions и параметр reverse (по умолчанию True). Возвращает новый список словарей, отсортированный по полю date.

python
Copy code
from src.processing.processing import sort_by_date

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-01'}
]

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)
# [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
#  {'id': 2, 'state': 'EXECUTED', 'date': '2022-01-01'}]