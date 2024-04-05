from typing import List

VACANT = "."  # can kill
QUEEN = "Q"


class Solution:
    '''
    Runtime
    Details
    51ms
    Beats 86.40%of users with Python3
    Memory
    Details
    16.70MB
    Beats 66.99%of users with Python3
    '''
    
    def copyBoard(self, board: List[str]):
        return [i[:] for i in board]

    def setCharAt(self, board: List[str], char: str, xi: int, yi: int):
        board[yi] = board[yi][:xi] + char + board[yi][xi + 1 :]

    def findQueens(
        self,
        board: List[str],
        col,
        res: List[List[List[str]]],
        leftRow: List[int],
        upperDiag: List[int],
        lowerDiag: List[int],
    ):
        x = len(board[0])
        y = len(board)
        n = len(board)

        if col == x:  # got the board we wanted
            # be sure to copy board as it later steps of backtracking can revert the changes
            res.append(self.copyBoard(board))
            return

        for yi in range(y):
            if (
                leftRow[yi] == 0
                and lowerDiag[yi + col] == 0
                and upperDiag[n - 1 + col - yi] == 0
            ):
                leftRow[yi] = 1
                lowerDiag[yi + col] = 1
                upperDiag[n - 1 + col - yi] = 1
                self.setCharAt(board, char=QUEEN, xi=col, yi=yi)

                self.findQueens(board, col + 1, res, leftRow, upperDiag, lowerDiag)

                leftRow[yi] = 0
                lowerDiag[yi + col] = 0
                upperDiag[n - 1 + col - yi] = 0
                self.setCharAt(board, char=VACANT, xi=col, yi=yi)

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [VACANT * n for _ in range(n)]
        leftRow = [0] * n
        upperDiag = [0] * (2 * n - 1)
        lowerDiag = [0] * (2 * n - 1)
        res = []
        self.findQueens(board, 0, res, leftRow, upperDiag, lowerDiag)
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
