class MinHeap:
    def __init__(self):
        pass

    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return (pos * 2) + 1

    def parent(self, pos):
        return pos // 2

    def isLeaf(self, pos, n):
        return pos > (n // 2)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(self, arr, n, i):
        lChild = self.left_child(i)
        rChild = self.right_child(i)

        smallest = i

        if lChild <= n and arr[smallest] > arr[lChild]:
            smallest = lChild
        if rChild <= n and arr[smallest] > arr[rChild]:
            smallest = rChild
        if smallest != i:
            self.swap(arr, i, smallest)

            self.heapify(arr, n, smallest)

    def getFirstLeadNode(self, n):
        return (n // 2) + 1

    def createHeap(self, arr):
        n = len(arr) - 1
        # start from the last non leaf node
        i = self.getFirstLeadNode(n) - 1

        while i > 0:
            self.heapify(arr, n, i)
            i -= 1

        return arr

    def insert(self, arr, n, new_val):
        n += 1
        arr.append(new_val)
        smallest = n

        # start going from bottom to top
        while smallest > 0:
            parent = self.parent(smallest)

            if arr[parent] > arr[smallest]:
                self.swap(arr, parent, smallest)

                smallest = parent
            else:
                return

    def pop(self, arr):
        n = len(arr) - 1

        # set the last element to the 1st element
        arr[1] = arr[n]

        # heapify for the 1st element to reposition
        self.heapify(arr, n - 1, 1)

        return arr[:n]


def main():
    heap = MinHeap()

    arr = [-1, 100, 20, 40, 50, 10]

    sort_array = [-1]
    for i in arr[1:]:
        print(sort_array)

        heap.insert(sort_array, len(sort_array) - 1, i)

    # arr = heap.createHeap(arr)

    # print(arr)
    # arr = heap.pop(arr)
    print(sort_array)


def minHeap(N: int, Q: [[]]) -> []:
    h = MinHeap()
    arr = [-1]
    for q in Q:
        if len(q) == 1:
            return arr[1]
        elif len(q) == 2:
            h.insert(arr, len(arr[1:]), q[1])


if __name__ == "__main__":
    N = 3

    Q = [[0, 2], [0, 1], [1]]

    print(f"Min element : {minHeap(N, Q)}")

    N = 2
    Q = [[0, 1], [1]]

    print(f"Min element : {minHeap(N, Q)}")
