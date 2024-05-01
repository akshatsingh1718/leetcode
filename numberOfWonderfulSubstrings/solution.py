"""
References: 
1. Good video: https://www.youtube.com/watch?v=1DdmbJj4xLE
"""

from collections import defaultdict


class Solution:
    '''
    TC: O(n) [for loop] + O(10) [xor from a-> j] ~ O(n)
    SC: O(n) [dict] + O(1) [cum_xor] + O(n) [count] ~ O(n)
    '''
    def wonderfulSubstrings(self, word: str) -> int:

        prv_xor = defaultdict(int)
        prv_xor[0] = 1  # for starting index
        cumulative_xor = 0
        count = 0

        for char in word:
            char_i = ord(char) - ord("a")
            cumulative_xor ^= 1 << char_i
            # print(cumulative_xor)

            # for even occurrences
            # if prv_xor.get(cumulative_xor, None) is not None:
            count += prv_xor[cumulative_xor]

            # for odd occurrences
            for i in range(0, 10):  # a -> j
                # if prv_xor.get(cumulative_xor ^ (1 << i)):
                count += prv_xor[cumulative_xor ^ (1 << i)]

            # increment the count
            # prv_xor[cumulative_xor] = prv_xor.get(cumulative_xor, 0) + 1
            prv_xor[cumulative_xor] += 1

        return count


class Solution2:  # using default dict
    def wonderfulSubstrings(self, word: str) -> int:

        prv_xor = defaultdict(int)
        prv_xor[0] = 1  # for starting index
        cumulative_xor = 0
        count = 0

        for char in word:
            char_i = ord(char) - ord("a")
            cumulative_xor ^= 1 << char_i

            # for even occurrences
            count += prv_xor[cumulative_xor]

            # for odd occurrences
            for i in range(0, 10):  # a -> j
                count += prv_xor[cumulative_xor ^ (1 << i)]

            # increment the count
            prv_xor[cumulative_xor] += 1

        return count


word = "aba"

output = 4
print(Solution().wonderfulSubstrings(word))
