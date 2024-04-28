from typing import *


class Solution:
    def minimumAddedInteger2(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()

        print(nums1)

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums2)):

                # ignore i and j
                if i == j:
                    continue
                k = 1
                ctr = 0
                diff = nums2[0] - (nums1[0] if k not in [i, j] else nums1[0 + 1])
                while k < len(nums2):
                    n1_val = nums1[k] if k not in [i, j] else nums1[k + 1]
                    if nums2[k] - n1_val == diff:
                        ctr += 1

                    diff = nums2[k] - n1_val
                    if i == 3 and j == 4:
                        print(n1_val)

                    k += 1

                if ctr == len(nums2) - 1:
                    print(i, j)
                    return diff
                    

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()

        # print(nums1)
        # print("====================")

        n1l = len(nums1)
        for i in range(n1l):
            for j in range(i, n1l):
                if i == j:
                    continue

                ar1 = nums1[:i] + nums1[i+1:j] + nums1[j+1:]

                # print(f"{i, j}", ar1)
                
                flag = True
                diff = nums2[0] - ar1[0]
                
                for k in range(1, len(nums2)):
                    # if i == 0 and j == 1:
                    #     print(diff, nums2[k] - ar1[k])
                    if nums2[k] - ar1[k] != diff:
                        flag = False
                        break
                if flag:
                    return diff


n1 = [4, 6, 3, 1, 4, 2, 10, 9, 5]
n2 = [5, 10, 3, 2, 6, 1, 9]
output = 0

# n1 = [4,20,16,12,8] # 0-> 4, 4->8
# n2 = [14,18,10]
# output = -2

print(Solution().minimumAddedInteger(n1, n2))
