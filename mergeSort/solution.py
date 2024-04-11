def merge(arr: list, low: int, mid: int, high: int):
    left = low
    right = mid + 1
    result = []

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1

    while left <= mid:
        result.append(arr[left])
        left += 1

    while right <= high:
        result.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = result[i - low]  # low is offset for result


def merge_sort(arr: list, low: int, high: int):
    if low == high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


a = [10, 1, 4, 2, -1]

merge_sort(a, 0, len(a) - 1)
print(a)
