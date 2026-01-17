from tasks.sorts.bubble_sort.solution import solution
import sys
import io


def capture_output(fn):
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        fn()
        return buffer.getvalue()
    finally:
        sys.stdout = old_stdout


def test_sorted():
    arr = [1, 2, 3, 4, 5]
    out = capture_output(lambda: solution(arr))
    assert out == "1 2 3 4 5\n"


def test_reverse():
    arr = [3, 2, 1]
    out = capture_output(lambda: solution(arr))
    assert out == "2 1 3\n1 2 3\n"


def test_duplicates():
    arr = [2, 2, 1]
    out = capture_output(lambda: solution(arr))
    assert out == "2 1 2\n1 2 2\n"


def test_negatives():
    arr = [7, -2, -1]
    out = capture_output(lambda: solution(arr))
    assert out == "-2 -1 7\n"


def test_many():
    arr = list(range(999, -1, -1))
    out = capture_output(lambda: solution(arr))
    lines = out.splitlines()
    assert lines[-1] == " ".join(map(str, range(1000)))
