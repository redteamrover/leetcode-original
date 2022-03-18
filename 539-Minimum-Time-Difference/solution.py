
from math import pi
from typing import List, Text


def minimum_difference(time_points: List[Text]) -> int:
    thetas = []

    for time_point in time_points:
        hour, minute = time_point.split(":")
        hour, minute = int(hour), int(minute)

        theta = hour * 60 + minute
        theta *= pi / 720

        thetas.append(theta)
    
    thetas = sorted(thetas)

    minimum = None

    for index, theta in enumerate(thetas):
        if index < len(thetas) - 1:
            difference = abs(theta - thetas[index + 1])
        else:
            difference = abs(theta - (2.0 * pi + thetas[0]))
        
        if minimum is None:
            minimum = difference
            continue
        
        minimum = difference if difference < minimum else minimum
    
    return round(minimum * (720 / pi))


def test_one_minute_difference() -> None:
    assert minimum_difference(["00:00","23:59"]) == 1


def test_repeated_time() -> None:
    assert minimum_difference(["00:00","23:59","00:00"]) == 0
