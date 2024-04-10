from typing import List

class Solution:
    '''
    TC: O(N logN) [sort] + O(N) [iterating over all indexes]
    SC: O(N) [store result] + O(N) [storing indexes]
    '''
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # sort the list
        deck.sort() # O(n logn)

        # create index list
        indexes = list(range(len(deck)))

        # results arr
        result = [0 for _ in range(len(deck))]

        while len(indexes) > 0:
            # pop 1st element
            ele = deck.pop(0)

            idx = indexes.pop(0)

            if len(indexes) > 0:
                move_to_back_ele = indexes.pop(0)
                indexes.append(move_to_back_ele)

            result[idx] = ele

        return result
    

# TS1
deck = [17,13,11,2,3,5,7]
output= [2,13,3,11,5,17,7]

# TS2
deck = [1,1000]
output= [1,1000]

print(Solution().deckRevealedIncreasing(deck))