'''
Problem: https://leetcode.com/problems/minimum-length-of-anagram-concatenation/
'''

from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        counts = Counter(s)

        n = len(s)

        # check all the possible string sizes
        for len_of_t_String in range(1, n// 2 +1):
            
            # check if the chosen string size can use all the chars of n 
            if n % len_of_t_String == 0:
                # freq % (num) here num cannot go beyond n // 2 since we want to make pairs 
                # if num goes > n//2 it means only 1 pair can be made
                # check if freq of each char 
                if all((freq % (n // len_of_t_String) ==0 for freq in counts.values())):
                    return len_of_t_String
                
        return n


print(Solution().minAnagramLength("aaaabbbbcccaaaa"))