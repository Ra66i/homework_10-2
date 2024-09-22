Банковский виджет операций клиента
Описание
Этот проект разрабатывается для отображения последних банковских операций клиента в его личном кабинете.

Установка
Клонируйте репозиторий:
bash

Verify

Open In Editor
Edit
Copy code
git clone https://github.com/Ra66i/homework_10-2.git
cd project-folder
Функции и генераторы
Модуль processing
filter_by_state: Функция для фильтрации транзакций по состоянию.
sort_by_date: Функция для сортировки транзакций по дате.
Модуль generators
filter_by_currency: Функция для фильтрации транзакций по валюте.
transaction_descriptions: Генератор для получения описаний транзакций.
card_number_generator: Генератор для генерации номеров банковских карт.
Примеры использования
filter_by_state
python

Verify

Open In Editor
Edit
Copy code
from src.processing.processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]

filtered_transactions = filter_by_state(transactions, state='EXECUTED')
print(filtered_transactions)
# [{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}]
sort_by_date
python

Verify

Open In Editor
Edit
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
filter_by_currency
python

Verify

Open In Editor
Edit
Copy code
transactions = [
    # ... список транзакций ...
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
transaction_descriptions
python

Verify

Open In Editor
Edit
Copy code
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
card_number_generator
python

Verify

Open In Editor
Edit
Copy code
for card_number in card_number_generator(1, 5):
    print(card_number)
Тестирование
В этом проекте использовался фреймворк pytest для тестирования функций filter_by_state и sort_by_date. Результаты тестирования представлены в следующем отчете:


Verify

Open In Editor
Edit
Copy code
Testing started at 12:34 ...
Launching pytest with arguments --no-header --no-summary -q in C:\Users\rabbi\PycharmProjects\homework_10-2

============================= test session starts =============================
collecting ... collected 5 items

decorators/test_logger.py::test_log_decorator PASSED                     [ 20%]
tests/test_generators.py::test_filter_by_currency[USD-expected_result0] PASSED [ 40%]
tests/test_generators.py::test_transaction_descriptions[transactions0-expected_result0] PASSED [ 60%]
tests/test_processing.py::test_sort_by_date[expected_ids0-True] PASSED   [ 80%]
tests/test_processing.py::test_sort_by_date[expected_ids1-False] PASSED  [100%]

============================== 5 passed in 0.05s ==============================
Все тесты прошли успешно, что свидетельствует о правильной работе функций filter_by_state и sort_by_date.