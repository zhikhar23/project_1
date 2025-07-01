import pandas as pd


def xslx_loader(path: str) -> list[dict]:
    """Функция обработки данных из файла формата xlsx"""
    excel_data = pd.read_excel(path)
    excel_data.dropna(how="all", inplace=True)
    return excel_data.to_dict(orient="records")
