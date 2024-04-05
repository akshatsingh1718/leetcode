from typing import List

OCCUPIED = "x"  # can kill
VACANT = "_"
QUEEN = "Q"


class Solution:
    def printBoard(self, board: List[str]):
        for row in board:
            print("  ".join(row))

    def markQueenSteps(self, board: List[str], xi: int, yi: int):
        x = len(board[0])
        y = len(board)

        # occupy neighbors
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                n_x = xi + i
                n_y = yi + j

                if 0 <= n_x < x and 0 <= n_y < y:
                    board[n_y][n_x] = OCCUPIED

        # occupy upper left diagonal
        n_x = xi - 1
        n_y = yi - 1
        while 0 <= n_x < x and 0 <= n_y < y:
            board[n_y][n_x] = OCCUPIED
            n_x -= 1
            n_y -= 1

        # occupy upper right diagonal
        n_x = xi + 1
        n_y = yi - 1
        while 0 <= n_x < x and 0 <= n_y < y:
            board[n_y][n_x] = OCCUPIED
            n_x += 1
            n_y -= 1

        # occupy lower left diagonal
        n_x = xi - 1
        n_y = yi + 1
        while 0 <= n_x < x and 0 <= n_y < y:
            board[n_y][n_x] = OCCUPIED
            n_x -= 1
            n_y += 1

        # occupy lower right diagonal
        n_x = xi + 1
        n_y = yi + 1
        while 0 <= n_x < x and 0 <= n_y < y:
            board[n_y][n_x] = OCCUPIED
            n_x += 1
            n_y += 1

    def copyBoard(self, board: List[str]):
        return [i[:] for i in board]

    def findEmptyPlace(self, board: List[str]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == VACANT:
                    return (i, j)
        return (-1, -1)

    def findQueens(self, board: List[str], noOfQueens: int):
        emptyY, emptyX = self.findEmptyPlace(board)
        if emptyX == -1 or board[emptyY][emptyX] != OCCUPIED:
            return None

        _board = self.copyBoard(board)
        _board[emptyY][emptyX] = QUEEN
        self.markQueenSteps(_board, xi=emptyX, yi=emptyY)

        board, queens = self.findQueens(_board, noOfQueens + 1)

        return board, queens

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[VACANT] * n for _ in range(n)]
        noOfQueens = n

        self.findQueens(board, noOfQueens = 0)

        self.printBoard(board)


def main():
    n = 4

    s = Solution()

    res = s.solveNQueens(n)

    # print(res)


if __name__ == "__main__":
    main()
