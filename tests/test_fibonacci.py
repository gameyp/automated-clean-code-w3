import automated_clean_code


def test_fibonacci():
    assert automated_clean_code.fibonacci(0) == 0
    assert automated_clean_code.fibonacci(1) == 1
    assert automated_clean_code.fibonacci(6) == 8


def test_fibonacci_large_number():
    assert automated_clean_code.fibonacci(30) == 832040
