from typing import List


class Solution:
    """
    Runtime
    Details
    140ms
    Beats 53.61%of users with Python3
    Memory
    Details
    21.16MB
    Beats 55.95%of users with Python3
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        for i in range(n):

            # check if merged is empty or 
            # if the the curr item start is gt the end time
            # of the last item added in the merged then start new interval check
            if len(merged) == 0 or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                # if curr item start is lte the end time of last interval added
                # item = merged.pop()
                # item[1] = max(item[1], intervals[i][1])
                # merged.append((item[0], item[1]))

                merged[-1][1] = max(merged[-1][1], intervals[i][1])

        return merged
    
def main():
    s = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    output = [[1, 6], [8, 10], [15, 18]]

    res = s.merge(intervals)
    print(res)


if __name__ == "__main__":
    main()
