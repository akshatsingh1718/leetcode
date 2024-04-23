from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def next_pin(seq: str, pos: int):
            pos_val = int(seq[pos])
            if pos_val == 9:
                return f"{seq[:pos]}0{seq[pos+1:]}"
            return f"{seq[:pos]}{pos_val+1}{seq[pos+1:]}"

        def prv_pin(seq: str, pos: int):
            pos_val = int(seq[pos])
            if pos_val == 0:
                return f"{seq[:pos]}9{seq[pos+1:]}"
            return f"{seq[:pos]}{pos_val-1}{seq[pos+1:]}"

        def dfs(seq: str, curr_steps: int, visited_routes: set):
            nonlocal target
            if seq in visited_routes:
                return

            if seq == target:
                print(curr_steps)
                return curr_steps

            temp_sequences = []
            for i in range(4):
                temp_sequences.append(next_pin(seq, pos=i))
                temp_sequences.append(prv_pin(seq, pos=i))

            print(temp_sequences)
            for temp_seq in temp_sequences:
                dfs(temp_seq, curr_steps + 1, visited_routes)

        return dfs("0000", 0, set(deadends + ["0000"]))


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
output = 6
print(Solution().openLock(deadends, target))
