from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        flag = True
        while flag:
            print(tickets)
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    flag = False
                    break
                if tickets[i] == 0:
                    continue
                
                tickets[i] -= 1
                seconds += 1

        return seconds
    

# tickets = [5,1,1,1]
# k = 0

tickets = [84,49,5,24,70,77,87,8]
k = 3
Expected = 154
print(Solution().timeRequiredToBuy(tickets, k))