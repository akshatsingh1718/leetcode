from typing import List


class Solution:
    """ """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            # if the last element we added already merged curr
            # element into its interval
            if len(merged) > 0 and merged[-1][1] >= end:
                continue

            # Here we will arrive if
            # 1. There is no interval added to the merged list
            # 2. The end time of the curr element is gt the last
            #    element's end time
            for j in range(i + 1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break

            merged.append((start, end))

        return merged


def main():
    s = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    output = [[1, 6], [8, 10], [15, 18]]

    res = s.merge(intervals)
    print(res)


if __name__ == "__main__":
    main()
