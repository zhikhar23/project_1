import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_value: str) -> str:
    """Функция маскировк цифр карты и счета"""
    value_split_list = input_value.split()
    if "Счет" in value_split_list:
        value_split_list[-1] = get_mask_account(value_split_list[-1])

    else:
        value_split_list[-1] = get_mask_card_number(value_split_list[-1])

    return " ".join(value_split_list)


def get_date(input_date: str) -> str:
    """Функция для возврата даты в нужном формате"""
    date = datetime.datetime.fromisoformat(input_date)
    return date.strftime("%d.%m.%Y")

