import time
import functools
import sys

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = f"{func.__name__} ok. Time: {end_time - start_time:.6f} sec. Result: {result}"
                log_to_file_or_console(log_message, filename)
            except Exception as e:
                log_message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                log_to_file_or_console(log_message, filename)
            return result
        return wrapper
    return decorator

def log_to_file_or_console(message, filename=None):
    if filename:
        try:
            with open(filename, 'a+') as file:
                file.write(message + '\n')
        except Exception as e:
            print(f"Ошибка записи в файл: {e}")
    else:
        print(message)

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

@log()
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

if __name__ == "__main__":
    my_function(1, 2)
    divide(10, 2)
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")