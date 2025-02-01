from collections import defaultdict


class Solution:
    def findValidPair(self, s: str) -> str:
        freq = defaultdict(int)
        for i, w in enumerate(s):
            freq[w] += 1

        is_candidate = []
        for i, w in enumerate(s):

            num = ord(w) - ord("0")
            is_candidate.append(num == freq[w])

        # check if the pair can be returned
        for i in range(len(s) - 1):
            if is_candidate[i] and is_candidate[i + 1] and s[i] != s[i + 1]:
                return f"{s[i]}{s[i+1]}"

        return ""


s = "2523533"
print(Solution().findValidPair(s))
