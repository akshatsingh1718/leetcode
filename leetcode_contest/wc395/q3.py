class Solution:
    # Wrong solution submitted by me
    def minEnd_Error(self, n: int, x: int) -> int:
        # first element
        last_num = x

        # second element element
        last_num += 1
        while last_num & x != x:
            last_num += 1
            print(last_num)

        for _ in range(2, n):
            # Error i did here was not incrementing last_num
            last_num = x | last_num

        return last_num

    def minEnd(self, n: int, x: int) -> int:
        # first element
        last_num = x

        # second element element
        # last_num += 1
        # while last_num & x != x:
        #     last_num += 1

        for _ in range(1, n):
            last_num = x | (last_num + 1)

        return last_num


n = 3
x = 4
output = 6

# TS2
# n = 2
# x = 7
# output= 15


res = Solution().minEnd(n, x)
# print(res)
