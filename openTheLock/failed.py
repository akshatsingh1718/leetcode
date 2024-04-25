from typing import List

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited_routes = set(deadends)
        min_step = 99999

        def dfs(seq: str, curr_steps: int):

            nonlocal target, visited_routes, min_step

            if seq in ["1000", "1100", "1200", "1201", "1202", "0202"]:
                print(f"{seq=} {curr_steps=}")
            if seq == target:
                min_step = min(min_step, curr_steps)

            for i in range(4):
                for delta in [-1, 1]:

                    sq = f"{seq[:i]}{(int(seq[i]) + delta) % 10}{seq[i+1:]}"

                    if sq not in visited_routes:
                        visited_routes.add(sq)
                        dfs(sq, curr_steps + 1)

        dfs("0000", 0)
        print(min_step)


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
output = 6

'''
This cannot be done by BFS as 1000 should have curr_step as 1 instead it is assigned as 9. See below the code output

seq='1000' curr_steps=9
seq='1200' curr_steps=87
seq='1100' curr_steps=98
seq='1202' curr_steps=8855
seq='0202' curr_steps=8856
seq='1201' curr_steps=9956
'''

print(Solution().openLock(deadends, target))
