class Solution:
    """GFG
    Problem Solved Successfully
    Test Cases Passed:
    203 /203
    Total Points Scored:
    4 /4
    Your Total Score:
    36
    Total Time Taken:
    0.48
    Your Accuracy:
    50%
    Attempts No.:
    2
    """

    def minimumPlatform(self, n, arr, dep):
        # store all the stations occupied here
        stations = []

        # sort the array and then iterate
        for ar, de in sorted(zip(arr, dep)):
            # assume the station has not been assigned
            isStationAllocated = False

            # check in stations if there is a station whose
            # departure time is lt current train arrival
            for i in range(len(stations)):
                if stations[i] < ar:
                    stations[i] = de
                    isStationAllocated = True
                    break
            
            # if the station is not allocated
            # meaning there is no occupied station whose departure is lt 
            # current train arrival time
            if not isStationAllocated:
                stations.append(de)

        return len(stations)


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
