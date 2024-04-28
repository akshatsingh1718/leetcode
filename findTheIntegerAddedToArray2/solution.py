from typing import List


class Solution:

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

                ar1 = nums1[:i] + nums1[i + 1 : j] + nums1[j + 1 :]

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
