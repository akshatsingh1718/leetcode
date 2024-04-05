from typing import List


class Solution:
    """
    Runtime
    Details
    920ms
    Beats 5.24%of users with Python3
    Memory
    Details
    21.03MB
    Beats 80.66%of users with Python3
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        visited = []
        merged = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            visited.append(i)

            for j in range(i, n):
                if j in visited:
                    i += 1
                    continue

                if start <= intervals[j][0] <= end:
                    visited.append(j)
                    end = max(end, intervals[j][1])
                    i += 1
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
