from typing import List
from time import perf_counter

class Solution:
    '''
    Runtime
    Details
    555ms
    Beats 9.62%of users with Python3
    Memory
    Details
    16.26MB
    Beats 90.21%of users with Python3
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

    def print(self, board):
        for i in board:
            print(i)

    def solve(self, board: List[List[str]]):
        n = len(board)

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.isValidPlace(board, j, i, str(k)):
                            board[i][j] = str(k)

                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."

                    return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)


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
