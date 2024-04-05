'''
Getting MaxTimeExceeding

visited is list of tuples for storing (x,y) instead use matrix of size mat given
as mark them 1 in visited[x][y]
'''
def visit(mat, x: int, y: int, queue: list, visited: list, onlyAdjacent=True):
    n = len(mat) - 1
    m = len(mat[0]) - 1

    # middle - top
    if mat[max(x - 1, 0)][y] != 0 and (max(x - 1, 0), y) not in visited:
        visited.append((max(x - 1, 0), y))
        queue.append((max(x - 1, 0), y))

    # middle bottom
    if mat[min(x + 1, n)][y] != 0 and (min(x + 1, n), y) not in visited:
        visited.append((min(x + 1, n), y))
        queue.append((min(x + 1, n), y))

    # middle left
    if mat[x][max(y - 1, 0)] != 0 and (x, max(y - 1, 0)) not in visited:
        visited.append((x, max(y - 1, 0)))
        queue.append((x, max(y - 1, 0)))

    # middle right
    if mat[x][min(y + 1, m)] != 0 and (x, min(y + 1, m)) not in visited:
        visited.append((x, min(y + 1, m)))
        queue.append((x, min(y + 1, m)))

    if onlyAdjacent:
        return

    # top left
    if (
        mat[max(x - 1, 0)][max(y - 1, 0)] != 0
        and (max(x - 1, 0), max(y - 1, 0)) not in visited
    ):
        visited.append((max(x - 1, 0), max(y - 1, 0)))
        queue.append((max(x - 1, 0), max(y - 1, 0)))

    # bottom left
    if (
        mat[min(x + 1, n)][max(y - 1, 0)] != 0
        and (min(x + 1, n), max(y - 1, 0)) not in visited
    ):
        visited.append((min(x + 1, n), max(y - 1, 0)))
        queue.append((min(x + 1, n), max(y - 1, 0)))

    # bottom right
    if (
        mat[min(x + 1, n)][min(y + 1, m)] != 0
        and (min(x + 1, n), min(y + 1, m)) not in visited
    ):
        visited.append((min(x + 1, n), min(y + 1, m)))
        queue.append((min(x + 1, n), min(y + 1, m)))

    # top right
    if (
        mat[max(x - 1, 0)][min(y + 1, m)] != 0
        and (max(x - 1, 0), min(y + 1, m)) not in visited
    ):
        visited.append((max(x - 1, 0), min(y + 1, m)))
        queue.append((max(x - 1, 0), min(y + 1, m)))


def visitForLoop(mat, x: int, y: int, queue: list, visited: list):
    n = len(mat)
    m = len(mat[0])
    for delrow in range(-1, 2):
        for delcol in range(-1, 2):
            row = x + delrow
            col = y + delcol

            if (
                0 <= row < n
                and 0 <= col < m
                and (row, col) not in visited
                and mat[row][col] != "0"
            ):
                visited.append((row, col))
                queue.append((row, col))


def bfs(mat, x, y, visited: list):
    visited.append((x, y))
    # visit neighbours
    q = list()
    q.append((x, y))

    while len(q) > 0:
        # got x and y
        nodeX, nodeY = q.pop(0)

        # visit all neighbours
        visitForLoop(mat, nodeX, nodeY, q, visited)


def noOfIslands(mat):
    count = 0
    visited = []
    for i, row in enumerate(mat):
        for j, col in enumerate(mat[i]):
            if (i, j) not in visited and mat[i][j] != "0":
                print(f"Not Visited: {i, j}")
                count += 1
                bfs(mat, i, j, visited)

    return count


def main():
    mat = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 1],
    ]

    mat = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    mat = [["1"]]

    mat = [
        ["1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "0", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "1"],
    ]

    # correct is 4
    correct = 4
    n = noOfIslands(mat)
    print(n)
    # assert n == correct, "Not Correct"


main()
