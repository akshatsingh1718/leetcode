# User function Template for python3
class Solution1:
    def CountPairs(self, N, k, arr):
        # code here
        def check(i, j):
            nonlocal arr, k
            return i < j and arr[i] == arr[j] and (i + j + 2) % k == 0

        counts = 0
        for i in range(N):
            for j in range(i, N):
                # if i == 2-1 and j == 4-1:
                #     print(f"{i=} {j=}", i < j , arr[i] == arr[j] , (i + j) % k == 0)
                if check(i, j):
                    # print(i, j)
                    counts = (counts + 1) % (1e9+7)

        return int(counts)

class Solution:
    def CountPairs(self, N, k, arr):
    # def count_pairs(arr, k):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Step 1: Create frequency map
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Step 2 and 3: Calculate pairs count
        total_pairs = 0
        
        for x in freq:
            count = freq[x]
            if count >= 2:
                # Calculate number of pairs for this element x
                pairs = (count * (count - 1)) // 2
                total_pairs = (total_pairs + pairs) % MOD
        
        return total_pairs


obj = Solution()
N = 5
k = 3
arr = [1, 2, 3, 2, 1]
expected = 2

# TS 2
N = 6
k = 4
arr = [1, 1, 1, 1, 1, 1]
expected = 3
print(obj.CountPairs(N, k, arr))
