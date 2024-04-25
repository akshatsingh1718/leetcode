class Solution:
    """
    TC: O(n * 26) [n for looping + 26 is worst case to check for all the alphabets as prv ones]
    SC: O(26)

        Algo:
    1. Create an array to store the seq values of each alphabet
    2. Iterate over each char of the s.
    3. Normalize the char value to 0->26 since value of "a" is 97, so we negate 97 from each char.
    4. get the range of permissible characters for the current char using k. For eg.- k=2 for char="d" will get the range of ["b", "c", "e", "f"] and k = 3 for char="a" will provide this range ["b", "c", "d"].
    5. Get the max value from the range and then for the current char index assign the value as max_value + 1.
    """

    def longestIdealString(self, s: str, k: int) -> int:

        # create arr for storing max seq values
        arr = [0 for _ in range(26)]

        n = len(s)
        i = n - 1
        while i >= 0:
            # check for the permissible range
            normalized_index = ord(s[i]) - ord("a")

            range_start = max(0, normalized_index - k)
            range_end = min(26, normalized_index + k) + 1

            max_value = max(arr[range_start:range_end])
            arr[normalized_index] = (max_value + 1)

            i -= 1

        return max(arr)


class Solution2:
    """
    TC: O(n^2)
    SC: O(n)

    Algo:

    """

    def longestIdealString(self, s: str, k: int) -> int:

        # create arr for storing max seq values
        arr = [0 for _ in range(26)]

        n = len(s)
        i = 0

        while i < n:
            # check for the permissible range
            normalized_index = ord(s[i]) - ord("a")

            range_start = max(0, normalized_index - k)
            range_end = min(26, normalized_index + k) + 1

            max_value = max(arr[range_start:range_end])
            arr[normalized_index] = (max_value + 1)

            # print(s[i], arr)
            i += 1

        return max(arr)


# TS1
s = "acfgbd"
k = 2
output = 4

# TS2
s = "abcd"
k = 3
output = 4

# TS3
s = "fabzcd"
k = 2

# TS4
s = "eduktdb"
k = 15
output = 5

# print("   ", end="")
# for c in [chr(i) for i in range(ord('a'), ord('a') + 26)]:
#     print(c, end=", ")
# print()
print(Solution().longestIdealString(s, k))
