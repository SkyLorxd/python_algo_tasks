from tasks.sorts.insertion_sort.solution import solution


def test_empty():
    arr = []
    solution(arr)
    assert arr == []


def test_single():
    arr = [10]
    solution(arr)
    assert arr == [10]


def test_sorted():
    arr = [1, 2, 3, 4, 5]
    solution(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_reverse():
    arr = [5, 4, 3, 2, 1]
    solution(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_duplicates_and_negatives():
    arr = [2, -1, 2, -1, 0]
    solution(arr)
    assert arr == [-1, -1, 0, 2, 2]


def test_many():
    arr = list(range(1000, 0, -1))
    solution(arr)
    assert arr == list(range(1, 1001))
