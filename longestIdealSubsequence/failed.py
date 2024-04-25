class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        running_seq = 0
        max_seq = 0
        last_char = s[0]
        hash_map = {s[0]: 1}

        for i, ele in enumerate(s[1:]):

            if abs(ord(last_char) - ord(ele)) <= k:
                running_seq += 1
            else:
                running_seq = 1

            max_seq = max(max_seq, running_seq)
            last_char = ele


class Solution1:
    def longestIdealString(self, s: str, k: int) -> int:

        running_seq = 0
        max_seq = 0
        last_char = s[0]
        # visited = {ord(s[0]): 1}
        visited = dict()

        for i, ele in enumerate(s):
            char = ord(ele)

            print(f"----------- char={ele} at {i=} ---------------")

            for key in list(visited.keys()):
                print(f"--> {chr(key)}")
                if abs(char - key) <= k:
                    visited[key] += 1
                    visited[char] = visited[key]

            if visited.get(char) is None:
                visited[char] = 1

            for key, val in visited.items():
                print(chr(key), val)

        return max(visited.values())


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

print(Solution1().longestIdealString(s, k))
