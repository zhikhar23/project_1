from collections import Counter

from csv_loader import loader
from processing import sort_by_date
from utils import get_transactions, process_bank_search
from widget import mask_account_card, get_date
from xslx_loader import xslx_loader


def main():
    while True:
        user_choice = input(
            """
            Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.]\n
            Выберите необходимый пункт меню:\n
            1. Получить информацию о транзакциях из JSON-файла\n
            2. Получить информацию о транзакциях из CSV-файла\n
            3. Получить информацию о транзакциях из XLSX-файла\n
            """
        )
        data = get_data(user_choice)
        if not data:
            continue
        else:
            break

    while True:
        user_filter = input(
            """
        Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n
        """
        )

        data = filter_data_by_status(user_filter, data)
        if not data:
            continue
        else:
            break

    while True:
        user_sort_state = input("Отсортировать операции по дате?")
        data = sort_by_user_state(user_sort_state, data)
        break

    while True:
        only_rub_filter = input("Выводить только рублевые транзакции? Да/Нет")
        data = filter_by_rub(only_rub_filter, user_choice, data)
        break

    while True:
        user_filter_by_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        data = filter_by_description(user_filter_by_description, data)
        break

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(data)}")
    for tr in data:
        print(f"{get_date(tr['date'])} {tr['description']}")
        print(f"{mask_account_card(tr["from"])}")
        amount = tr.get("amount") if tr.get("amount") else tr.get("operationAmount").get("amount")
        print(f"Сумма {amount}")


def get_data(user_choice: str) -> list[dict]:
    data = []
    if user_choice == "1":
        data = get_transactions("../data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif user_choice == "2":
        data = loader("../data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif user_choice == "3":
        data = xslx_loader("../data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.")
    return data


def filter_data_by_status(user_filter: str, data: list) -> list | None:
    if user_filter.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Введите корректный статус EXECUTED, CANCELED, PENDING")
        return None
    else:
        return [tr for tr in data if tr.get("state") == user_filter]


def sort_by_user_state(user_sort_state, date):
    if user_sort_state.lower() == "да":
        while True:
            user_sort = input("Отсортировать по возрастанию или по убыванию?")
            if user_sort.lower() == "по возрастанию":
                date = sort_by_date(date, ascending=False)
                break

            elif user_sort.lower() == "по убыванию":
                date = sort_by_date(date, ascending=True)
                break
            else:
                continue
    return date


def process_bank_operations(data: list[dict], categories: list) -> dict:
    category = [i.get("description") for i in data]
    category_count = Counter(category)


def filter_by_rub(only_rub_filter, user_choice, data):
    if only_rub_filter.lower() == "да":
        if user_choice == "1":
            res = []
            for tr in data:
                currency_code = tr.get("operationAmount").get("currency").get("code")
                if currency_code and currency_code == "RUB":
                    res.append(tr)
            return res
        data = [tr for tr in data if tr.get("currency_code") == "RUB"]
    return data


def filter_by_description(filter_state, data):
    if filter_state == "да":
        user_search = input("Введите слово для поиска")
        data = process_bank_search(data, user_search)
    return data


if __name__ == "__main__":
    main()
