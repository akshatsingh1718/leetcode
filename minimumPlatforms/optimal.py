class Solution:
    """GFG
    Test Cases Passed:
    203 /203
    Your Total Score:
    36
    Total Time Taken:
    0.12
    Correct Submission Count:
    2
    """

    def minimumPlatform(self, n, arr, dep):
        # sort both the arrays
        arr.sort()
        dep.sort()

        print(f"{arr=}")
        print(f"{dep=}")

        # set the initial res and platform needed
        max_platform_needed = 1
        platform_needed = 1

        arri = 1
        depj = 0

        while arri < n and depj < n:
            # check if the current arr is gt prv departure

            if arr[arri] <= dep[depj]:
                platform_needed += 1
                arri += 1
            elif arr[arri] > dep[depj]:
                platform_needed -= 1
                depj += 1

            max_platform_needed = max(max_platform_needed, platform_needed)
        return max_platform_needed


def main():
    s = Solution()
    n = 6
    arr = ["0900", "0940", "0950", "1100", "1500", "1800"]
    dep = ["0910", "1200", "1120", "1130", "1900", "2000"]
    output = 3

    res = s.minimumPlatform(n, arr, dep)

    print(res)

    assert res == output, "Not Matching"


if __name__ == "__main__":
    main()
