
from typing import List, Text


def fizz_buzz_string(n: int) -> Text:
    if n % 15 == 0:
        return "FizzBuzz"
    
    if n % 3 == 0:
        return "Fizz"

    if n % 5 == 0:
        return "Buzz"
    
    return str(n)


def fizz_buzz(n: int) -> List[Text]:
    return [fizz_buzz_string(i) for i in range(1, n+1)]


def test_example_one() -> None:
    assert fizz_buzz(3) == ["1", "2", "Fizz"]


def test_example_two() -> None:
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_example_three() -> None:
    assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
