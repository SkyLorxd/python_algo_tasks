from tasks.recursion.binary_search.solution import solution


def test_found_with_duplicates():
    arr = [1, 2, 2, 4, 7]
    idx = solution(arr, 2)
    assert idx in (1, 2)


def test_not_found():
    arr = [1, 3, 5]
    assert solution(arr, 2) == -1


def test_empty_array():
    assert solution([], 10) == -1


def test_single_element_found():
    assert solution([5], 5) == 0


def test_single_element_not_found():
    assert solution([5], 3) == -1


def test_negative_values():
    arr = [-10, -5, -1, 0, 3]
    assert solution(arr, -5) == 1
    assert solution(arr, 2) == -1


def test_large_array():
    n = 1000000
    arr = list(range(n))
    assert solution(arr, 0) == 0
    assert solution(arr, n - 1) == n - 1
    assert solution(arr, n // 2) == n // 2
    assert solution(arr, n + 1) == -1
