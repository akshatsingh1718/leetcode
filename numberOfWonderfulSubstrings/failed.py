class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        word_counts = dict()
        res = 0
        odd_counts = 0

        for char in word:
            word_counts[char] = word_counts.get(char, 0 ) + 1


            if word_counts[char] % 2 != 0: # is odd
                odd_counts += 1
            else:
                odd_counts -= 1

            if odd_counts < 2:
                print(char, odd_counts)
                res += 1

        res += len(word) # single word substring
            

        return res


word = "aba"
output= 4
print(Solution().wonderfulSubstrings(word))