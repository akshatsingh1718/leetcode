"""
references:
1. https://leetcode.com/problems/minimum-array-end/solutions/5082310/bit-interweaving/
2. https://leetcode.com/problems/minimum-array-end/solutions/5083945/visualized-explain-by-images-step-by-step-filling-zero-bits-approach/
"""


class Solution:
    """
    TC: O(64) [64 bit number]
    SC: O(2 * 64) [for storing bits as string of list]
    """

    def minEnd(self, n: int, x: int) -> int:

        xbin_list = list(bin(x)[2:])
        nbin_list = list(bin(n - 1)[2:])

        curr_n = len(nbin_list) - 1

        for i in range(len(xbin_list) - 1, -1, -1):

            if xbin_list[i] == "1":
                continue

            xbin_list[i] = nbin_list[curr_n]
            curr_n -= 1

            if curr_n == -1:
                break

        # copy rest of the elements

        if curr_n != -1:
            xbin_list = nbin_list[: curr_n + 1] + xbin_list

        return int("".join(xbin_list), 2)


print(Solution().minEnd(n=3, x=4))
