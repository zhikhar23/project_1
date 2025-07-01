import json
import logging
import os
import re
from collections import Counter

logging.basicConfig(encoding="utf-8", filemode="w")
utils_log = logging.getLogger("utils_log")
utils_log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_handler.setFormatter(formatter)
utils_log.addHandler(file_handler)


def get_transactions(json_path: str) -> list:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    if not os.path.exists(json_path):
        utils_log.info("Путь к файлу не найден")
        return []
    try:
        with open(json_path, encoding="utf-8") as f:
            try:
                utils_log.info("Пробуем получить данные из файла")
                data = json.load(f)
            except json.JSONDecodeError:
                utils_log.info("Неверный формат данных")
                return []
            if isinstance(data, list):
                utils_log.info("Загружаем данные")
                return data
            else:
                return []
    except (OSError, IOError):
        utils_log.error("Неуспешный запрос")
        return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    pattern = re.compile(search, flags=re.IGNORECASE)

    for tr in data:
        if "description" in tr:
            description = tr["description"]
            if pattern.search(description):
                result.append(tr)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    res = []
    for tr in data:
        if tr["description"].lower() in categories:
            res.append(tr)
    a = [tr["description"] for tr in res]
    return Counter(a)
