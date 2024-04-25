# My Solution: https://leetcode.com/problems/n-th-tribonacci-number/solutions/5066519/faster-lesser-bfs-approach-using-memoization-recursion/

class Solution:
    """
    TC: O(3^n) [as each recursive call invoke 3 more calls]
    SC: O(1)

    Algo (Recursion)
    """

    def tribonacci(self, n: int) -> int:

        def trib(n: int) -> int:
            if n <= 0:
                return 0
            if n in [1, 2]:
                return 1

            return trib(n - 1) + trib(n - 2) + trib(n - 3)

        return trib(n)


class Solution2:
    """
    Time complexity:
    O(n)
    First we will find the tribonacci from 3->n'th value since 0, 1 and 2 values we already know. After finding all the values from 3->n recursing for n-2 and n-3 will not take much time as we are storing value for each number in visited map.

    Space complexity:
    O(n) [for storing tribonacci number values from 0->n]
    
    Algo (Recursion + DP)
    """

    def tribonacci(self, n: int) -> int:

        # Store the visited nums and
        # initially set 0, 1 and 2 as we alreday know their tribonaccies
        visited = {0: 0, 1: 1, 2: 1}

        def trib(n: int) -> int:
            # declare that visited will not be a local to trib and
            # it is an global variable
            nonlocal visited
            # if already visited then return the memoized/saved result
            if visited.get(n) is not None:
                return visited[n]

            # Find the tribonacci value for the previous three numbers
            # from visited numbers if present or recurse and find their values and store in the visited
            visited[n - 3] = visited.get(n - 3, trib(n - 3))
            visited[n - 2] = visited.get(n - 2, trib(n - 2))
            visited[n - 1] = visited.get(n - 1, trib(n - 1))

            return visited[n - 1] + visited[n - 2] + visited[n - 3]

        res = trib(n)
        return res


n = 31
# 53798080
print(Solution2().tribonacci(n))
