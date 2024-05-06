from collections import defaultdict, Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        def computeGCD(x, y):
            while y:
                x, y = y, x % y
            return abs(x)

        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        counts_list = list(counts.values())

        if len(counts_list) == 1:
            return 1

        if len(counts) == len(s):
            return len(s)

        gcd = computeGCD(counts_list[0], counts_list[1])
        for i in range(2, len(counts_list)):
            gcd = computeGCD(gcd, counts_list[i])

        return gcd


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

print(Solution().minAnagramLength("cdef")) # E = 4
print(Solution().minAnagramLength("jjj")) # E = 1
print(Solution().minAnagramLength("xxe")) # E= 3


