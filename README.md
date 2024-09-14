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


# Модуль generators

Модуль `generators` содержит функции и генераторы для работы с массивами транзакций. Он позволяет финансовым аналитикам быстро и удобно находить нужную информацию о транзакциях и проводить анализ данных.

## Функция `filter_by_currency`

Функция `filter_by_currency` принимает на вход список словарей, представляющих транзакции, и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной. Например:

```python
transactions = [
    # ... список транзакций ...
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

Вывод:

{
  "id": 939719570,
  "state": "EXECUTED",
  "date": "2018-06-30T02:08:58.425572",
  "operationAmount": {
      "amount": "9824.07",
      "currency": {
          "name": "USD",
          "code": "USD"
      }
  },
  "description": "Перевод организации",
  "from": "Счет 75106830613657916952",
  "to": "Счет 11776614605963066702"
}
{
  "id": 142264268,
  "state": "EXECUTED",
  "date": "2019-04-04T23:20:05.206878",
  "operationAmount": {
      "amount": "79114.93",
      "currency": {
          "name": "USD",
          "code": "USD"
      }
  },
  "description": "Перевод со счета на счет",
  "from": "Счет 19708645243227258542",
  "to": "Счет 75651667383060284188"
}

Генератор transaction_descriptions
Генератор transaction_descriptions принимает список словарей с транзакциями и возвращает описание каждой операции по очереди. Например:

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

Вывод:

Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации

Генератор card_number_generator
Генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999. Например:

for card_number in card_number_generator(1, 5):
    print(card_number)

Вывод:

0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005