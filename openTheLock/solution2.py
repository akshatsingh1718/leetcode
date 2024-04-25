from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 
        
        visited_routes = set(deadends + ["0000"])

        queue = [("0000", 0)]

        # until queue is empty
        while len(queue) > 0:

            # unpack combination and moves it took to reach the combination
            combination, moves = queue.pop(0)

            # if we found the target then return the combination
            if combination == target:
                return moves

            # For loop for each index
            for i in range(4):
                # change of number in +1 and -1 direction
                for delta in [-1, +1]:
                    new_no = (int(combination[i]) + delta) % 10 
                    # create the next seq
                    seq = f"{combination[:i]}{ new_no }{combination[i+1:]}"
                    # check if seq already visited
                    if seq not in visited_routes:
                        visited_routes.add(seq)
                        queue.append((seq, moves + 1))

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
output = 6


print(Solution().openLock(deadends, target))
