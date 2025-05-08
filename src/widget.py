import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_value: str) -> str:
    """Функция маскировк цифр карты и счета"""
    if len(input_value)!=0:
        value_split_list = input_value.split()
    else:
        return "Неверный номер карты/счёта"
    if "Счет" in value_split_list and len(value_split_list[-1]) == 20 and value_split_list[-1].isdigit():
        value_split_list[-1] = get_mask_account(value_split_list[-1])
        return " ".join(value_split_list)
    else:
        if len(value_split_list[-1]) == 16 and value_split_list[-1].isdigit():
            value_split_list[-1] = get_mask_card_number(value_split_list[-1])
            return " ".join(value_split_list)
        else:
            return "Неверный номер карты/счёта"




def get_date(input_date: str) -> str:
    """Функция для возврата даты в нужном формате"""
    try:
        date = datetime.datetime.fromisoformat(input_date)
    except ValueError:
          return "Неверный формат даты"
    else:
        return date.strftime("%d.%m.%Y")

