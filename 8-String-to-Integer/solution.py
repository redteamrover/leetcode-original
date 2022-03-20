
from re import search
from string import digits, whitespace
from typing import Text


def atoi(string: Text, n: int = 0) -> int:
    """Convert String to Integer"""
    # Parse the input string for the sign and value.
    result = search(r"^(?:\s*)(\+|\-)?([0-9]+)", string)

    # If the regex failed to match the input string, we do
    # not have a valid input string, and we should therefore
    # return zero.
    if not result:
        return 0

    # Split the result into its constituent components.
    sign, value = result.groups()
    
    # Apply the sign to the value, if necessary.
    result = -1 * int(value) if sign == "-" else int(value)

    # Clamp the number to an acceptable range.
    if result > (2**31 - 1):
        result = 2**31 - 1
    elif result < -(2**31):
        result = -(2**31)
    
    return result


def test_example_one() -> None:
    assert atoi("42") == 42


def test_example_two() -> None:
    assert atoi("   -42") == -42


def test_example_three() -> None:
    assert atoi("4193 with words") == 4193


def test_example_four() -> None:
    assert atoi("words and 987") == 0


def test_example_five() -> None:
    assert atoi("-91283472332") == -2147483648


def test_example_six() -> None:
    assert atoi("+-12") == 0
