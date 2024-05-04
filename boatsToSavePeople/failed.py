from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        if len(people) == 1:
            return 1

        people.sort()

        limit_temp = limit
        count = 0
        for num in people:
            limit_temp -= num

            if limit_temp < 0:
                count += 1
                limit_temp = limit- num
            if limit_temp == 0:
                limit_temp = limit
                count += 1

            print(f"{count=} {num=} {limit_temp=}")

        print(limit_temp)
        if limit_temp > 0 and limit_temp != limit:
            count += 1

        return count
    
people = [2,4]
limit = 5

people = [5,1,4,2] # 1, 2, 4, 5
limit = 6

print(Solution().numRescueBoats(people, limit))