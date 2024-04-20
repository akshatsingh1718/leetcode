# Your task is to complete this function
# Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        max_seq = 0

        hash_map = dict()
        running_sum = 0

        for i, num in enumerate(arr):
            running_sum += num

            if running_sum == 0:
                max_seq = i + 1

            elif hash_map.get(running_sum, None) is not None:
                max_seq = max(max_seq, i - hash_map[running_sum])
            else:
                hash_map[running_sum] = i

        return max_seq


# {
# Driver Code Starts
if __name__ == "__main__":
    ob = Solution()
    n = 8
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print(ob.maxLen(n, arr))
