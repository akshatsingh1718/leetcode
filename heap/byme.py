class Heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)  # idx =0 will be ignored

    def parent(self, idx):
        return idx // 2

    def left_child(self, idx):
        return 2 * idx

    def right_child(self, idx):
        return (2 * idx) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size


    def insert(self, val):
        index = self.size + 1

        if index == self.maxsize:
            print("[ERROR] Heap Max size reached")
            return

        # increase size of heap
        self.size += 1

        self.heap[index] = val

        # index should be gt 1 as it indicated parent pos
        # and hence we reached the root of the heap
        while index > 1:
            if self.heap[index] > self.heap[self.parent(index)]:
                # swap index and parent if parent is lt current index idx
                self.swap(index, self.parent(index))

                index = self.parent(index)

            else:
                return  # all good parent is gt its child

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def swapElement(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def delete(self):
        if self.size == 0:
            print("Nothing to delete")
            return

        # replace first with last element
        self.heap[1] = self.heap[self.size]

        # decrease the size of the array
        self.size -= 1

        index = 1  # set index to root to reposition the new root element
        while index <= self.size:
            # find the left and right child of the index
            lIndex = self.left_child(index)
            rIndex = self.right_child(index)
            largest = index

            # check if left child index exists and is gt current largest
            if lIndex <= self.size and self.heap[lIndex] > self.heap[largest]:
                largest = lIndex
            # check if right child index exists and is gt current largest
            if rIndex <= self.size and self.heap[rIndex] > self.heap[largest]:
                largest = rIndex

            if index == largest:
                return  # done !

            # swap index with largest
            self.swap(index, largest)

            # set the index to curr largest
            index = largest

    def heapify(self, heap, n, index):
        """
        This will repositioned the index you have passed
        """
        # get both left and right child of the index
        lChild = self.left_child(index)
        rChild = self.right_child(index)

        # assume the given index is the largest amongst its child's
        largest = index
        # check with left child from largest
        if lChild <= n and heap[lChild] > heap[largest]:
            largest = lChild
        # check with right child from largest
        if rChild <= n and heap[rChild] > heap[largest]:
            largest = rChild

        # if there is new largest element found then swap
        if largest != index:
            self.swapElement(heap, largest, index)
            # start heapify for the new largest index we just have repositioned
            self.heapify(heap, n, largest)
        else:
            return

    def print(self):
        print(self.heap[1 : self.size + 1])

    def getStartLeftNode(self, sizeOfHeap: int):
        return (sizeOfHeap // 2) + 1

    def createHeap(self, arr):
        n = len(arr) - 1
        i = h.getStartLeftNode(n) - 1  # get the last node which is not a leaf

        while i > 0:
            h.heapify(arr, n, i)
            i -= 1

        return arr

    def heap_sort(self, arr):
        # create heap
        arr = self.createHeap(arr)
        n = len(arr) - 1

        while n > 1:
            ## replace the 1st / root of the heap with the last element
            self.swapElement(arr, n, 1)
            n -= 1

            # Now largest element is at the last of the array
            # make arr heap again as the last element is now at the top/root
            self.heapify(arr, n, 1)

        return arr


## main
h = Heap(10)

arr = [-1, 54, 53, 55, 52, 50]
n = len(arr)

print(arr)

h.heap_sort(arr)

print(arr)
