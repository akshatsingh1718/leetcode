'''
Runtime
Details
322ms
Beats 48.68%of users with Python3
Memory
Details
18.89MB
Beats 78.11%of users with Python3
'''

def visit(mat, x: int, y: int, queue: list, visited: list, onlyAdjacent=True):

    n = len(mat) - 1
    m = len(mat[0]) - 1

    # middle - top
    if mat[max(x - 1, 0)][y] != "0" and not visited[max(x - 1, 0)][y]:
        queue.append((max(x - 1, 0), y))
        visited[max(x - 1, 0)][y] = 1

    # middle bottom
    if mat[min(x + 1, n)][y] != "0" and not visited[min(x + 1, n)][y]:
        visited[min(x + 1, n)][y] = 1
        queue.append((min(x + 1, n), y))

    # middle left
    if mat[x][max(y - 1, 0)] != "0" and not visited[x][max(y - 1, 0)]:
        visited[x][max(y - 1, 0)] = 1
        queue.append((x, max(y - 1, 0)))

    # middle right
    if mat[x][min(y + 1, m)] != "0" and not visited[x][min(y + 1, m)]:
        visited[x][min(y + 1, m)] = 1
        queue.append((x, min(y + 1, m)))

    if onlyAdjacent:
        return

    # top left
    if (
        mat[max(x - 1, 0)][max(y - 1, 0)] != "0"
        and not visited[max(x - 1, 0)][max(y - 1, 0)]
    ):
        visited[max(x - 1, 0)][max(y - 1, 0)] = 1
        queue.append((max(x - 1, 0), max(y - 1, 0)))

    # bottom left
    if (
        mat[min(x + 1, n)][max(y - 1, 0)] != "0"
        and not visited[min(x + 1, n)][max(y - 1, 0)]
    ):
        visited[min(x + 1, n)][max(y - 1, 0)] = 1
        queue.append((min(x + 1, n), max(y - 1, 0)))

    # bottom right
    if (
        mat[min(x + 1, n)][min(y + 1, m)] != "0"
        and not visited[min(x + 1, n)][min(y + 1, m)]
    ):
        visited[min(x + 1, n)][min(y + 1, m)] = 1
        queue.append((min(x + 1, n), min(y + 1, m)))

    # top right
    if (
        mat[max(x - 1, 0)][min(y + 1, m)] != "0"
        and not visited[max(x - 1, 0)][min(y + 1, m)]
    ):
        visited[max(x - 1, 0)][min(y + 1, m)] = 1
        queue.append((max(x - 1, 0), min(y + 1, m)))


def bfs(mat, x, y, visited: list):
    q = list()
    q.append((x, y))

    while len(q) > 0:
        # got x and y
        nodeX, nodeY = q.pop(0)

        # visit all neighbours
        visit(mat, nodeX, nodeY, q, visited)


def noOfIslands(mat):
    count = 0
    n, m = len(mat), len(mat[0])

    visited = [[0] * m for _ in range(n)]
    for i, row in enumerate(mat):
        for j, col in enumerate(mat[i]):
            if not visited[i][j] and mat[i][j] != "0":
                print(f"Not Visited: {i, j}")
                visited[i][j] = 1
                count += 1
                bfs(mat, i, j, visited)

    return count


def main():
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
