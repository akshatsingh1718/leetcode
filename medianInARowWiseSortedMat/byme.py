

def median(matrix: [[int]], m: int, n: int) -> int:
    arr = matrix[0]

    for row in matrix[1:]:
        arr += row

    arr.sort()

    return arr[(m * n)//2]

    


def main():
    mat = [
        [1, 5, 7, 9, 11],
        [2, 3, 4, 8, 9],
        [4, 11, 14, 19, 20],
        [6, 10, 22, 99, 100],
        [7, 15, 17, 24, 28],
    ]
    m = len(mat)
    n = len(mat[0])

    output = 10

    
    print(median(mat, m, n))


if __name__ == "__main__":
    main()
