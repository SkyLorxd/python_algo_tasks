def solution(arr: list[int]) -> None:
    n = len(arr)
    needs_sort = False

    for _ in range(n - 1):
        swapped = False

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if swapped:
            needs_sort = True
            print(*arr)
        else:
            break

    if not needs_sort:
        print(*arr)
