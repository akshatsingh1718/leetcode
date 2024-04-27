class Solution:
    """

    =======================
    Time & Space Complexity
    =======================
    n = len(ring)
    m = len(key)

    TC: O(n * m * n) [n * m = recursion; n = for loop over ring values]
    SC: O(n * m)


    =======================
    Algo
    =======================
    Top Down DP
    """

    def findRotateSteps(self, ring: str, key: str) -> int:

        cache = dict()

        def find_steps(ring_idx: int, key_idx: int):
            nonlocal ring, key

            # if we reached the end of the key then we are arrived at the stopage
            if key_idx == len(key):
                return 0  # 0 because we no distance should be convered from the last value in our key

            # if alredy visited
            if cache.get((ring_idx, key_idx)) is not None:
                return cache[(ring_idx, key_idx)]
            
            # assuming our total distance will take infinity to reach at the solution
            min_steps = float("inf")

            # iterate over ring values and check for the desired next value of key
            for i in range(len(ring)):

                # if we found our desired key
                if ring[i] == key[key_idx]:
                    # find both the distances from current ring index (ring_idx) to the idx "i" we found to be matching with out key value
                    total_distance = (
                        min(
                            abs(ring_idx - i), # from ring_idx -> i
                            len(ring) - abs(ring_idx - i) # the other way around
                        )
                        + 1 # add one more step to press the button
                        + find_steps(i, key_idx + 1) # move to the next key value
                    )

                    min_steps = min(min_steps, total_distance) # get the min distance
            cache[(ring_idx, key_idx)] = min_steps

            return min_steps

        return find_steps(ring_idx=0, key_idx=0)


ring = "godding"
key = "gd"
output = 4

# TS2
# ring = "godding"
# key = "godding"
# output= 13

# TS3
# ring = "xrrakuulnczywjs"
# key = "jrlucwzakzussrlckyjjsuwkuarnaluxnyzcnrxxwruyr"

# TS4
ring = "abcde"
key = "ade"
output= 6

print(Solution().findRotateSteps(ring, key))
