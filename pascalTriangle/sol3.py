from typing import List


class Solution:
    """
    Runtime
    Details
    39ms
    Beats 70.21%of users with Python3
    Memory
    Details
    16.35MB
    Beats 36.28%of users with Python3
    """

    def get_binomial_coeff_till(self, n: int) -> int:
        """
        In sol1 we are finding out the binomial coefficient of a particular index
        in the pascal triangle. For calculating the last item of any line in pascal
        triangle we are actually finding out the preceding items along the way.
        """
        res = 1
        arr = [res]

        for i in range(n):
            res *= n - i
            res /= i + 1

            arr.append(int(res))

        return arr

    def generate(self, numRows: int) -> List[List[int]]:
        for line in range(0, numRows):
            print(self.get_binomial_coeff_till(line))


def main():
    s = Solution()
    s.generate(5)


if __name__ == "__main__":
    main()
