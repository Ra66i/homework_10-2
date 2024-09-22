import pytest
from io import StringIO
import sys
import time
import functools
import os

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                output = f"{func.__name__} ok. Time: {execution_time:.6f} sec. Result: {result}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(output + "\n")
                else:
                    print(output)
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                output = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(output + "\n")
                else:
                    print(output)
                raise
        return wrapper
    return decorator

def test_log_decorator():
    @log()
    def test_function(x, y):
        return x + y

    old_stdout = sys.stdout
    sys.stdout = StringIO()
    test_function(1, 2)
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert "test_function ok. Time:" in output
    assert "Result: 3" in output

    @log()
    def test_function_with_error(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ZeroDivisionError("division by zero")

    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        test_function_with_error(1, 0)
    except ZeroDivisionError:
        output = sys.stdout.getvalue().strip()
        sys.stdout = old_stdout
        assert "test_function_with_error error: ZeroDivisionError" in output
        assert "Inputs: (1, 0)" in output

    @log(filename="testlog.txt")
    def test_function_with_file(x, y):
        return x + y

    test_function_with_file(5, 5)
    with open("testlog.txt", "r") as file:
        output = file.read().strip()
    assert "test_function_with_file ok. Time:" in output
    assert "Result: 10" in output
    os.remove("testlog.txt")  # удалить файл после теста