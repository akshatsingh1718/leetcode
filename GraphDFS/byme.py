from typing import List


def traverse(
    node: int, adj: List[List[int]], visited: List[int], dfs: List[int]
) -> None:
    visited[node] = 1
    dfs.append(node)
    for n in adj[node]:
        if not visited[n]:
            traverse(n, adj, visited, dfs)


def traverseDFS(n: int, adj: List[List[int]]) -> List[int]:
    dfs = []
    visited = [0] * n
    traverse(0, adj, visited, dfs)
    return dfs


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

    dfs = traverseDFS(n, adj)
    print(dfs)


if __name__ == "__main__":
    main()
