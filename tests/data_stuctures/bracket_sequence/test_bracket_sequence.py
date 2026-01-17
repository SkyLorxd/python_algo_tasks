from tasks.data_stuctures.bracket_sequence.solution import solution


def test_many_correct():
    assert solution("{[()]}") is True


def test_pair_correct():
    assert solution("()") is True


def test_empty_string():
    assert solution("") is True


def test_wrong_order():
    assert solution("([)]") is False


def test_many_open():
    assert solution("(((") is False


def test_many_close():
    assert solution("())") is False


def test_many():
    s = "(" * 100000 + ")" * 100000
    assert solution(s) is True
