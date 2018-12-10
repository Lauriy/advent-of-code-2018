import pytest

from day_3 import Day3, my_input


@pytest.mark.parametrize('test_input, expected_result', [
    (['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 4),
    (my_input, None)
])
def test_first(test_input, expected_result):
    day3 = Day3()
    if expected_result is not None:
        assert day3.first(test_input) == expected_result
    else:
        answer = day3.first(test_input)
        assert isinstance(answer, int)
        print(answer)


@pytest.mark.parametrize('test_input, expected_result', [
    (['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 3),
    (my_input, None)
])
def test_second(test_input, expected_result):
    day3 = Day3()
    if expected_result is not None:
        assert day3.second(test_input) == expected_result
    else:
        answer = day3.second(test_input)
        assert isinstance(answer, int)
        print(answer)
