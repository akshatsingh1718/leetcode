class Solution:
    '''
    Runtime
    Details
    44ms
    Beats 49.27%of users with Python3
    Memory
    Details
    16.20MB
    Beats 96.40%of users with Python3
    '''
    def helper(self, x: float, n: float) -> float:
        if n == 0:
            return 1

        elif n % 2 == 0:
            return self.helper(x * x, n // 2)
        else:
            return x * self.helper(x * x, (n - 1) // 2)

    def myPow(self, x: float, n: int) -> float:
        isNegative = False
        if n < 0:
            isNegative = True

        ans = self.helper(x, abs(n))
        return 1 / ans if isNegative else ans


def main():
    s = Solution()

    x = 2.000
    n = 2

    res = s.myPow(x, n)

    print(res)


if __name__ == "__main__":
    main()
