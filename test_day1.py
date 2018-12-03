import pytest

from day1 import Day1, my_input


@pytest.mark.parametrize('test_input, expected_result', [
    ([1, 1, 1], 3),
    ([1, 1, -2], 0),
    ([-1, -2, -3], -6),
    (my_input, None)
])
def test_first(test_input, expected_result):
    day1 = Day1()
    if expected_result is not None:
        assert day1.first(test_input) == expected_result
    else:
        answer = day1.first(test_input)
        assert isinstance(answer, int)
        print(answer)


@pytest.mark.parametrize('test_input, expected_result', [
    ([-1, 1], 0),
    ([3, 3, 4, -2, -4], 10),
    ([-6, 3, 8, 5, -6], 5),
    ([7, 7, -2, -7, -4], 14),
    (my_input, None)
])
def test_second(test_input, expected_result):
    day1 = Day1()
    if expected_result is not None:
        assert day1.second(test_input) == expected_result
    else:
        answer = day1.second(test_input)
        assert isinstance(answer, int)
        print(answer)
