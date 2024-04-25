class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        res = 0

        for i in range(n):
            for j in range(i, n):

                xor = 0
                for k in range(i, j + 1):
                    xor ^= A[k]

                if xor == B:
                    res += 1

        return res


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    '''
    
    [1, 4, 5, 6]

    i = 0
        j = (i=0 -> n=4)
            j = 1

    TC: O(n^2)
    SC: O(1)
    '''
    def solve(self, A, B):

        n = len(A)
        res = 0

        for i in range(n):
            # initilize the xor 
            xor = 0

            for j in range(i, n):
                # at each stage we compute xor from (i -> n)
                xor ^= A[j]

                if xor == B:
                    res += 1

        return res


A = [4, 2, 2, 6, 4]
B = 6
output = 4


# A = [5, 6, 7, 8, 9]
# B = 5
# output = 2

print(Solution().solve(A, B))
