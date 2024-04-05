from typing import List
from time import perf_counter


class Solution:
    '''
    Runtime
    Details
    475ms
    Beats 14.36%of users with Python3
    Memory
    Details
    16.50MB
    Beats 41.14%of users with Python3
    '''
    def isValidPlace(self, board: List[List[str]], xi: int, yi: int, char: str):
        n = len(board)
        start_idx = [0, 3, 6]

        start_x = start_idx[xi // 3]
        start_y = start_idx[yi // 3]

        for i in range(start_x, start_x + 3):
            for j in range(start_y, start_y + 3):
                if board[j][i] == char:
                    return False

        for i in range(0, n):
            if board[yi][i] == char:
                return False

        for i in range(0, n):
            if board[i][xi] == char:
                return False

        return True

    def solve(self, board: List[List[str]], xi: int, yi: int):
        n = len(board)

        if xi == n and yi == n - 1:
            return True

        if xi == n:
            xi = 0
            yi += 1

        if board[yi][xi] == ".":
            for ch in range(1, 10):
                ch = str(ch)

                if self.isValidPlace(board, xi, yi, ch):
                    board[yi][xi] = ch

                    if self.solve(board, xi + 1, yi):
                        return True
                    else:
                        board[yi][xi] = "."
            return False
        else:
            return self.solve(board, xi + 1, yi)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, xi=0, yi=0)


def main():
    s = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    t1_start = perf_counter() 

    s.solveSudoku(board)

    # Stop the stopwatch / counter
    t1_stop = perf_counter()
    
    print("Elapsed time during the whole program in seconds:",
                                            t1_stop-t1_start)


    for bi in board:
        print(bi)


if __name__ == "__main__":
    main()
