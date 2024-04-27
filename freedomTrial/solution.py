class Solution:

    '''
    Throws TLE

    TC: (i * j ^ 2 ) [i is len of key and j is len of ring]
    '''
    def findRotateSteps(self, ring: str, key: str) -> int:

        def rotate_clockwise(word_to_find: str, ring_index: int):
            nonlocal ring

            steps = 0
            while ring[ring_index] != word_to_find:
                ring_index = (ring_index + 1) % len(ring)
                steps += 1

            return (ring_index, steps + 1)

        def rotate_anticlockwise(word_to_find: str, ring_index: int):
            nonlocal ring

            steps = 0
            while ring[ring_index] != word_to_find:
                # ring_index = (len(ring) - (ring_index % len(ring))) % len(ring)
                ring_index -= 1
                if ring_index == -1:
                    ring_index = len(ring) - 1

                steps += 1

            return (ring_index, steps + 1)

        def find_steps(i: int, j: int, counts: int):
            nonlocal key, ring


            if i == len(key):
                return counts
            
            (index_clockwise, steps_clockwise) = rotate_clockwise(key[i], ring_index=j)
            (index_anticlockwise, steps_anticlockwise) = rotate_anticlockwise(
                key[i], ring_index=j
            )

            cnt1 = find_steps(i=i + 1, j=index_clockwise, counts=steps_clockwise + counts)
            cnt2 = find_steps(
                i=i + 1, j=index_anticlockwise, counts=steps_anticlockwise + counts
            )

            res= min(cnt1, cnt2)

            return res

        return find_steps(i=0, j=0, counts=0)


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
# ring = "abcde"
# key = "ade"
# output= 6

print(Solution().findRotateSteps(ring, key))
