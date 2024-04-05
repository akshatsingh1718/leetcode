from typing import List


class Solution:
    '''
    i) Find the whole pascal triangle as shown above.
    ii) Find just the one element of a pascal's triangle given row number and column number in O(n) time.
    iii) Find a particular row of pascal's triangle given a row number in O(n) time.
    '''
    def binomial_coeff(self, n: int, k: int) -> int:
        # store the result
        res = 1

        k = (n - k) if (k > n - k) else k

        for i in range(k):
            res *= n - i
            res /= i + 1

        return int(res)

        """
        ===========================
        Case: When k > n - k    (k = 7)
        ===========================
        k = 7
        n = 10

        n - k = 10 - 7 => 3

        k > n - k => 7 > 3 => True
            Then
            k = n - k => k = 3

        
        |------ Factorial example ------|
        nCr = 10 C 7 => 10! / (7!) (10-7)! => 10! / (7!) (3)!

        Here k = 7 and our for loop will iterate from (1-7) so we will be doing more compute
        than if we had took k = 3.

        Q. Why to choose K as 3 and not 7 ?
        A. If k is 7 then numerator will go from 10 - 4 (excluding 3) as after that 3, 2 and 1 mul will be
            cancelled by 3!.
           If k is 3 then numerator will go from 10 - 8 as after that 7,6...1 mul will be cancelled by 7!
        
        ===========================
        Case: When k > n - k    (k = 3)
        ===========================
        n = 10
        k = 3

        n - k = 10 - 3 => 7

        k > n - k => 3 > 7 => False
            Then
            k = k => k = 3


        ===========================
        Case: When k > n - k    (k = 2)
        ===========================
        n = 10
        k = 2

        n - k = 10 - 2 => 8

        k > n - k => 2 > 8 => False
            Then
            k = k => k = 2


        +++++++++++++++++++++++++++
                Conclusion
        +++++++++++++++++++++++++++
        If (n - k) is gt k then k will be (n - k)
        If (n - k) is lt k then k will be k only.
        """

    def generate(self, numRows: int) -> List[List[int]]:
        for line in range(0, numRows):
            for i in range(0, line + 1):
                print(self.binomial_coeff(line, i), " ", end="")
            print()


def main():
    s = Solution()
    s.generate(5)


if __name__ == "__main__":
    main()
