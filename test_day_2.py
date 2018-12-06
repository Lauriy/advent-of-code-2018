import pytest

from day_2 import Day2, my_input


@pytest.mark.parametrize('test_input, expected_result', [
    (['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'], 12),
    (my_input, None)
])
def test_first(test_input, expected_result):
    day2 = Day2()
    if expected_result is not None:
        assert day2.first(test_input) == expected_result
    else:
        answer = day2.first(test_input)
        assert isinstance(answer, int)
        print(answer)


@pytest.mark.parametrize('test_input, expected_result', [
    (['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'], 'fgij'),
    (my_input, None)
])
def test_second(test_input, expected_result):
    day2 = Day2()
    if expected_result is not None:
        assert day2.second(test_input) == expected_result
    else:
        answer = day2.second(test_input)
        assert isinstance(answer, str)
        print(answer)
