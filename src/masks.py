import logging

logging.basicConfig(encoding="utf-8", filemode="w")
masks_logger = logging.getLogger("masks_log")
masks_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Неверный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает замаскированный номер счёта"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Неверный номер счёта"


get_mask_card_number("4564545665511256")
get_mask_account("v5454v6d5v4d5fvfv")
