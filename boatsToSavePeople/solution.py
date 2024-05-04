from typing import List


class Solution:
    '''
    TC : O(n logn) [sorting] + O(n) [for looping]
    '''
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        if len(people) == 1:
            return 1

        people.sort() # sort the array
        n = len(people)
        l = 0
        r = n - 1
        count = 0

        while l <= r:
            # check if the sum of biggest and smallest is less than or equal to limit
            if people[l] + people[r] <= limit:
                l += 1 # then increase the left

            # if some is getting greater than limit it means we need to decrease the sum
            # which can be done by decrementing the right pointer which will surely give
            # smaller value than prv sum as the array is sorted
            count += 1
            r -= 1

        return count


# TS 1
people = [2, 4]
limit = 5
output = 2

# TS 2
# people = [5, 1, 4, 2]  # 1, 2, 4, 5
# limit = 6
# output = 2


print(Solution().numRescueBoats(people, limit))
