from typing import List

VACANT = "."  # can kill
QUEEN = "Q"


class Solution:
    '''
    Runtime
    Details
    207ms
    Beats 8.90%of users with Python3
    Memory
    Details
    16.74MB
    Beats 66.99%of users with Python3
    '''
    def printBoard(self, board: List[str]):
        for row in board:
            print("  ".join(row))

    def isSafe(self, board: List[str], xi: int, yi: int):
        x = len(board[0])
        y = len(board)

        # check neighbors for queen
        # for i in [-1, 0, 1]:
        #     for j in [-1, 0, 1]:
        #         if i == 0 and j == 0:
        #             continue
        #         n_x = xi + i
        #         n_y = yi + j

        #         if 0 <= n_x < x and 0 <= n_y < y and board[n_y][n_x] == QUEEN:
        #             return False

        # check horizontal for queen
        for n_x in range(x):
            if n_x == xi:
                # continue
                break # no need to check after xi as we have not visited those cols
            if board[yi][n_x] == QUEEN:
                return False

        # check vertical for queen (no need to check as 1 col can have at max 1 queen)
        # for n_y in range(y):
        #     if n_y == yi:
        #         continue
        #     if board[n_y][xi] == QUEEN:
        #         return False

        # check upper left diagonal for queen
        n_x = xi - 1
        n_y = yi - 1
        while 0 <= n_x < x and 0 <= n_y < y:
            if board[n_y][n_x] == QUEEN:
                return False
            n_x -= 1
            n_y -= 1

        # check upper right diagonal for queen (not visited the right portion yet! )
        # n_x = xi + 1
        # n_y = yi - 1
        # while 0 <= n_x < x and 0 <= n_y < y:
        #     if board[n_y][n_x] == QUEEN:
        #         return False
        #     n_x += 1
        #     n_y -= 1

        # check lower left diagonal for queen
        n_x = xi - 1
        n_y = yi + 1
        while 0 <= n_x < x and 0 <= n_y < y:
            if board[n_y][n_x] == QUEEN:
                return False
            n_x -= 1
            n_y += 1

        # check lower right diagonal for queen ( not visited the right area)
        # n_x = xi + 1
        # n_y = yi + 1
        # while 0 <= n_x < x and 0 <= n_y < y:
        #     if board[n_y][n_x] == QUEEN:
        #         return False
        #     n_x += 1
        #     n_y += 1

        return True

    def copyBoard(self, board: List[str]):
        return [i[:] for i in board]

    def setCharAt(self, board: List[str], char: str, xi: int, yi: int):
        board[yi] = board[yi][:xi] + char + board[yi][xi + 1 :]

    def findQueens(self, board: List[str], col, res: List[List[List[str]]]):
        x = len(board[0])
        y = len(board)

        if col == x:  # got the board we wanted
            # be sure to copy board as it later steps of backtracking can revert the changes
            res.append(self.copyBoard(board))
            return

        for yi in range(y):
            if self.isSafe(board, xi=col, yi=yi):
                self.setCharAt(board, char=QUEEN, xi=col, yi=yi)
                self.findQueens(board, col + 1, res)
                self.setCharAt(board, char=VACANT, xi=col, yi=yi)

    def formatOutput(self, board: List[List[str]]) -> List[str]:
        return ["".join(i) for i in board]

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [VACANT * n for _ in range(n)]
        res = []
        self.findQueens(board, 0, res)
        return res


def main():
    n = 4

    s = Solution()

    res = s.solveNQueens(n)

    for ri in res:
        print("-------------------\n")
        print(ri)
        # s.printBoard(ri)


if __name__ == "__main__":
    main()
