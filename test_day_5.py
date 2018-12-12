import pytest

from day_5 import Day5, my_input


@pytest.mark.parametrize('test_input, expected_result', [
    ('aA', 0),
    ('abBA', 0),
    ('abAB', 4),
    ('aabAAB', 6),
    ('dabAcCaCBAcCcaDA', 10),
    (my_input, None)
])
def test_first(test_input, expected_result):
    day5 = Day5()
    if expected_result is not None:
        assert day5.first(test_input) == expected_result
    else:
        answer = day5.first(test_input)
        assert isinstance(answer, int)
        print(answer)


@pytest.mark.parametrize('test_input, expected_result', [
    ('dabAcCaCBAcCcaDA', 4),
    (my_input, None)
])
def test_second(test_input, expected_result):
    day5 = Day5()
    if expected_result is not None:
        assert day5.second(test_input) == expected_result
    else:
        answer = day5.second(test_input)
        assert isinstance(answer, int)
        print(answer)
