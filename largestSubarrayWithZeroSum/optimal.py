# Your task is to complete this function
# Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        max_seq = 0
        for i in range(n):
            curr_seq = 0
            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                curr_seq += 1

            if curr_sum == 0: # check sum
                max_seq = max(max_seq, curr_seq)


        return max_seq

# {
# Driver Code Starts
if __name__ == "__main__":
    ob = Solution()
    n = 8
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print(ob.maxLen(n, arr))
