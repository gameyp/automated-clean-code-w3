import automated_clean_code


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert automated_clean_code.add_numbers(1, 2) == 3


def test_add_negative_numbers():
    assert automated_clean_code.add_numbers(-1, -2) == -3


def test_add_zero():
    assert automated_clean_code.add_numbers(0, 0) == 0


def test_add_large_numbers():
    assert automated_clean_code.add_numbers(1000000, 2000000) == 3000000


def test_add_positive_and_negative_numbers():
    assert automated_clean_code.add_numbers(5, -3) == 2


def test_add_decimal_numbers():
    assert automated_clean_code.add_numbers(1.5, 2.5) == 4.0


def test_add_large_and_small_numbers():
    assert automated_clean_code.add_numbers(100, 0.001) == 100.001


def test_add_same_numbers():
    assert automated_clean_code.add_numbers(5, 5) == 10


def test_add_number_and_negative():
    assert automated_clean_code.add_numbers(5, -5) == 0


def test_add_very_large_numbers():
    assert automated_clean_code.add_numbers(1e308, 1e308) == float("inf")


def test_add_very_small_numbers():
    assert automated_clean_code.add_numbers(1e-308, 1e-308) == 2e-308


def test_add_none():
    try:
        automated_clean_code.add_numbers(None, None)
    except TypeError:
        assert True
    else:
        assert False
