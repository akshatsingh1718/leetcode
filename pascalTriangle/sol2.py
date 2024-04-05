from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[0] * numRows] * numRows

        for line in range(0, numRows):
            for i in range(0, line + 1):
                if i == 0 or i == line:
                    res = 1
                else:
                    res = arr[line - 1][i - 1] + arr[line - 1][i]

                arr[line][i] = res
                print(f"{res} ", end="")

            print()


def main():
    s = Solution()
    s.generate(5)


if __name__ == "__main__":
    main()
