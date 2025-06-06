def log(filename=None):
    def my_decor(func):
        def wrapper(*args, **kwargs):
            """Функция для изменения результаты другой функции"""
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} \nok \n")
                else:
                    print(f"{func.__name__} ok")
                    return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message)

        return wrapper

    return my_decor


@log(filename="log.txt")
def my_function(x, y):
    return x / y


my_function(1, 0)
