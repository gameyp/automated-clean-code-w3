def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome.

    Args:
      s (str): a string

    Returns:
      (bool). True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number.

    Args:
      n (int): an integer

    Returns:
      (int). The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
