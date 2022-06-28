# Тестовое задание Finstar #

### - получать список товаров, купленных одним покупателем. ###
http://127.0.0.1:8080/product/?receipt__user__id=3
### - получать список магазинов для одного покупателя.  ###
http://127.0.0.1:8080/user_shop/?user=3
### - получать сумму покупок в интервале дат ###
http://127.0.0.1:8080/receipt/sum_receipt_in_interval/?end_date=1998-01-01
http://127.0.0.1:8080/receipt/sum_receipt_in_interval/?start_date=1990-01-01&end_date=2023-01-01
### - сумма чеков за все время ###
http://127.0.0.1:8080/receipt/sum_receipt_in_interval/
### - получать список чеков с товарами в интервале дат или на конкретную дату ###
http://127.0.0.1:8080/receipt_list/sum_receipt_in_interval/?end_date=1998-01-01
http://127.0.0.1:8080/receipt_list/sum_receipt_in_interval/?start_date=1990-01-01&end_date=2023-01-01
http://127.0.0.1:8080/receipt_list/sum_receipt_in_interval/?date=2022-06-27
### - загружать чеки в формате json. Будет плюсом, если будет возможность пакетной ###
### отправки (несколько чеков сразу). ###
### Метод POST ###
http://127.0.0.1:8080/receipt/ в формате:
```json
{
    "user": {"name": "Имя"},
    "shop": {"name": "Название магазина"},
    "number_receipt": 3,
    "time_issuance": "08:15:19",
    "date_issuance": "2000-01-01",
    "sum_receipt": 10000,
    "product": {
        "name": "Карп Карпыч",
        "quantity": 3,
        "price": 1000
    }
}
```
или список таких объектов
```json
[{
    "user": {"name": "Имя"},
    "shop": {"name": "Название магазина"},
    "number_receipt": 3,
    "time_issuance": "08:15:19",
    "date_issuance": "2000-01-01",
    "sum_receipt": 10000,
    "product": {
        "name": "Карп Карпыч",
        "quantity": 3,
        "price": 1000
    }
},
{
    "user": {"name": "Имя"},
    "shop": {"name": "Название магазина"},
    "number_receipt": 3,
    "time_issuance": "08:15:19",
    "date_issuance": "2000-01-01",
    "sum_receipt": 10000,
    "product": {
        "name": "Карп Карпыч",
        "quantity": 3,
        "price": 1000
    }
}]
```