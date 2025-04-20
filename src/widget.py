import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция маскировк цифр карты и счета"""
    data = data.split()
    if "Счет" in data:
        data[-1] = get_mask_account(data[-1])

    else:
        data[-1] = get_mask_card_number(data[-1])

    return " ".join(data)


data = "Счет 35383033474447895560"
# print (mask_account_card(data))


def get_date(date: str) -> str:
    y = datetime.datetime.fromisoformat(date)
    return y.strftime("%d.%m.%Y")


date = "2024-03-11T02:26:18.671407"
print(get_date(date))
