class DisjointSet:
    def __init__(self, V: int):
        self.V = V
        self.rank = [0] * V
        self.parent = list(range(V))

    def find(self, x: int) -> int:
        """
        Find the parent of the x using path compression
        """
        x_parent = self.parent[x]
        if x_parent == x:
            return x

        self.parent[x] = self.find(x_parent)
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        Union of x and y
        """
        x_parent = self.parent[x]
        y_parent = self.parent[y]
        if x_parent == y_parent:
            return

        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        if self.rank[x_parent] == self.rank[y_parent]:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
