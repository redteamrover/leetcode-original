
def reverse(x: int) -> int:
    negative = True if x < 0 else False
    x = abs(x)
    result = 0

    while x:
        result *= 10
        result += (x % 10)
        x = x // 10
    
    if result > (2**31 - 1):
        return 0
    elif result < -(2**31):
        return 0

    return -1 * result if negative else result


def test_example_one() -> None:
    assert reverse(123) == 321


def test_example_two() -> None:
    assert reverse(-123) == -321


def test_example_three() -> None:
    assert reverse(120) == 21


def test_overflow() -> None:
    assert reverse(1000999 * (2**31)) == 0


def test_underflow() -> None:
    assert reverse(-1000999 * (2**31)) == 0
