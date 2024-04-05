from typing import List


def traverseBFS(n: int, adj: List[List[int]]):
    visited = [0] * n
    visited[0] = 1 # mark first node as visited

    q = list()
    q.append(0)

    bfs = []

    while len(q) > 0:

        node = q.pop(0)

        bfs.append(node)

        for it in adj[node]:
            if not visited[it]:
                visited[it] = 1
                q.append(it)

    return bfs


def main():
    adj = [
        [1],  # 0
        [2, 6],  # 1
        [1, 3, 4],  # 2
        [2],  # 3
        [2, 5, 7],  # 4
        [4, 7],  # 5
        [1, 7, 8],  # 6
        [5, 6],  # 7
        [6],  # 8
    ]

    n = len(adj)

    bfs = traverseBFS(n, adj)
    print(bfs)


if __name__ == "__main__":
    main()