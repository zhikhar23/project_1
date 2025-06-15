import os
import requests
from dotenv import load_dotenv
from src.utils import get_transactions


load_dotenv()
API_KEY = os.getenv("API_KEY")
payload = {}
headers = {"apikey": API_KEY}

currency_code = "RUB"

def transaction_summ(transact, code):
    """Функция обрабатывающая транзакции и возвращающая сумму всех транзакций в рублях
    если транзакция в USD или EUR ,то конвертирует их по курсу через API"""

    if not transact.get("operationAmount") :
        return "Неподходящая транзакция"

    if transact["operationAmount"]["currency"].get("code"):
        transaction_code = transact.get("operationAmount").get("currency").get("code")
        amount = float(transact.get("operationAmount").get("amount"))

        if transaction_code == code:
            return float(transact["operationAmount"]["amount"])

        elif transaction_code == "USD" or transaction_code == "EUR":
              url = f"https://api.apilayer.com/exchangerates_data/convert?to={code}&from={transaction_code}&amount={amount}"
              response = requests.get(url, headers=headers, data=payload)
              if response.status_code == 200:
                   result = response.json().get("result")
                   if isinstance(result, (int, float)):
                        return result
              else:
                    return f"Не успешный запрос, код ошибки: {response.status_code}"
for transact in get_transactions(json_path="..\data\operations.json"):
    print(transaction_summ(transact,currency_code))