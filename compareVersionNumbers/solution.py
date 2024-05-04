class Solution:
    """
    n1 =len(version1)
    n2 =len(version2)
    TC: O( max(n1, n2) )
    SC: O(n1 + n2) [worst case when there is only number and no zeros and "."]
    """

    def compareVersion(self, version1: str, version2: str) -> int:

        i = 0
        j = 0
        n1 = len(version1)
        n2 = len(version2)

        while i < n1 or j < n2:

            # skip 0's
            while i < n1 and version1[i] == "0":
                i += 1

            while j < n2 and version2[j] == "0":
                j += 1

            # convert the str num to int num
            num1 = ""
            num2 = ""
            while i < n1 and version1[i] != ".":
                num1 += version1[i]
                i += 1

            while j < n2 and version2[j] != ".":
                num2 += version2[j]
                j += 1

            # check the integer value of both the strings
            num1 = 0 if len(num1) == 0 else int(num1)
            num2 = 0 if len(num2) == 0 else int(num2)

            # check if one number is greater than other
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

            i += 1
            j += 1

        return 0


version1 = "1.0.1"
version2 = "1"
output = 1
print(Solution().compareVersion(version1, version2))
