from typing import List


def countSmallerThanEqualTo(arr: 'List[int]', num: int):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= num:
            # low += 1
            low = mid + 1
        else:
            # high -= 1
            high = mid - 1
    return low


def median(matrix: [[int]], m: int, n: int) -> int:
    low = 0
    high = 1e9

    while low <= high:
        mid = low + (high - low) // 2

        cnt = 0

        for i in range(m):
            cnt += countSmallerThanEqualTo(matrix[i], mid)

        # print(f"{mid=} | {cnt=} | {low=} | {high=}"), print("=" * 30)

        if cnt <= (n * m) / 2:
            low = mid + 1
        else:
            high = mid - 1

    return int(low)


def main():
    # mat = [
    #     [1, 5, 7, 9, 11],
    #     [2, 3, 4, 8, 9],
    #     [4, 11, 14, 19, 20],
    #     [6, 11, 22, 99, 100],
    #     [7, 15, 17, 24, 28],
    # ]

    mat=[
    [1, 5, 7, 9, 11], 
    [2, 3, 4, 8, 9], 
    [4, 11, 14, 19, 20], 
    [6, 10, 22, 99, 100], 
    [7, 15, 17, 24, 28]
    ] 
    m = len(mat)
    n = len(mat[0])

    output = 10

    print(median(mat, m, n))


if __name__ == "__main__":
    main()

"""
arr = [1, 2, 3, 5, 6, 7, 8]


"""
