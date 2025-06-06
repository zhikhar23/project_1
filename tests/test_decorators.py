import pytest

from src.decorators import log


@log(filename=None)
def my_function(x, y):
    """Тестовая функция с декоратором"""
    return x / y


def test_decorator_log():
    """Тестирование декоратора без выхода ошибки"""
    @log(filename=None)
    def my_function_(x, y):
        return x / y
    assert my_function(6, 3) == 2

def test_decorator_capsys_1(capsys):
    """Тестирование декоратора без ошибки через capsys"""
    my_function(6,0)
    captured = capsys.readouterr()
    assert "ok" in captured.out

def test_dec_zerodev(capsys):
    """тест с делением на ноль"""
    my_function(1,0)
    captured=capsys.readouterr()
    assert "Zero" in captured.out

def test_dec_error(capsys):
    """Тест на ошибку по типу данных """
    my_function("2","f")
    captured=capsys.readouterr()
    assert captured.out=="my_function error: TypeError. Inputs: ('2', 'f'), {}\n\n"
