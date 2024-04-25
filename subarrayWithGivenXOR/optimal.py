class Solution:
    '''
    TC: O(n)
    SC: O(n) [for storing n xor operations]
    
    '''
    def solve(self, A, B):

        count = 0
        # This is when our nth element is equal to B which will give 0 as xor since B^B = 0
        prv_seq = {0 : 1}
        running_xor = 0

        for num in A:
            running_xor ^= num

            negation_xor = running_xor ^ B

            if prv_seq.get(negation_xor, None) is not None:
                count += prv_seq[negation_xor]

            prv_seq[running_xor] = prv_seq.get(running_xor, 0) + 1

        return count


A = [4, 2, 2, 6, 4]
B = 6
output = 4


A = [5, 6, 7, 8, 9]
B = 5
output = 2

print(Solution().solve(A, B))
