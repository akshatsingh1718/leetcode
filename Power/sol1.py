class Solution:
    """
    Runtime
    Details
    38ms
    Beats 77.91%of users with Python3
    Memory
    Details
    16.12MB
    Beats 96.40%of users with Python3
    """

    def myPow(self, x: float, n: int) -> float:
        isNegative = False

        if n < 0:
            isNegative = True
            n *= -1

        ans = 1

        while n:
            print(f"{n=}\t{x=}\t{ans=}")
            if n % 2 == 0:
                x = x * x
                n /= 2
            else:
                ans = ans * x
                n -= 1

        return (1 / ans) if isNegative else ans


def main():
    s = Solution()

    x = 2.000
    n = -2

    res = s.myPow(x, n)

    print(res)


if __name__ == "__main__":
    main()
