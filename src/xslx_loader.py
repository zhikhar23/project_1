import pandas as pd


def xslx_loader(path: str) -> list[dict]:
    excel_data = pd.read_excel(path)
    return excel_data.to_dict(orient="records")

a=xslx_loader('../data/transactions_excel.xlsx')
print(a)