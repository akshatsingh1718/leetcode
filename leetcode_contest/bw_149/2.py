from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # get the empty places
        room_status = [1] * eventTime
        # 1 : Free
        # 0 : Occupied
        for st, et in zip(startTime, endTime):
            for i in range(st, et):
                room_status[i] = 0

        free_i = 0
        meeting_i = 0
        while k:

            # make the first meeting to  the left most as we can
            while free_i < eventTime and room_status[free_i] == 0:
                free_i += 1

            # print(free_i)

            # now free_i is free
            # now get the meeting which is next to it
            while meeting_i < len(startTime) and startTime[meeting_i] > free_i:
                meeting_i += 1

            if meeting_i >= len(startTime):
                break

            # now we have a meeting_i which is ahead of free_i
            # make free_i + endTime[meeting_i] occupied
            for _ in range(free_i, endTime[meeting_i]):
                if free_i >= eventTime:
                    break
                room_status[free_i] = 0
                free_i += 1

            temp_i = free_i
            for _ in range(free_i, endTime[meeting_i]):
                if temp_i >= eventTime:
                    break
                room_status[temp_i] = 1  # free
                temp_i += 1
            # while free_i <= endTime[meeting_i]:
            #     room_status[free_i] = 1
            #     free_i += 1

            k -= 1
        print(room_status)

        res = 0
        count = 0
        for i in range(len(room_status)):
            if room_status[i] == 0:  # occupied
                res = max(res, count)
                count = 0
            else:
                count += 1
        return res


class Solution:
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)

        # Calculate the initial free time intervals
        free_intervals = []
        free_intervals.append(startTime[0] - 0)  # Free time before the first meeting
        for i in range(1, n):
            free_intervals.append(
                startTime[i] - endTime[i - 1]
            )  # Free time between meetings
        free_intervals.append(
            eventTime - endTime[-1]
        )  # Free time after the last meeting

        # If no meetings, the entire event time is free
        if n == 0:
            return eventTime

        # If k is 0, return the maximum free time without rescheduling
        if k == 0:
            return max(free_intervals)

        # To maximize the largest free time, we need to merge the smallest gaps
        # We can reschedule up to k meetings to merge gaps
        # We will try to merge the smallest gaps first

        # Sort the free intervals (excluding the first and last if they are fixed)
        # The first and last free intervals are fixed because we cannot move meetings outside the event
        # So we only consider the gaps between meetings
        gaps = free_intervals[1:-1]
        gaps.sort()

        # Merge the smallest gaps by rescheduling meetings
        # Each rescheduling allows us to merge two gaps into one
        # We can perform at most k reschedulings
        for _ in range(k):
            if len(gaps) == 0:
                break
            # Merge the smallest gap
            smallest_gap = gaps.pop(0)
            # The new gap will be the sum of the smallest gap and the next smallest gap
            if len(gaps) > 0:
                gaps[0] += smallest_gap

        # The largest free time is the maximum of the remaining gaps and the fixed boundaries
        max_free = max(free_intervals[0], free_intervals[-1])
        if len(gaps) > 0:
            max_free = max(max_free, max(gaps))

        return max_free


# Example usage
eventTime = 5
k = 1
startTime = [1, 3]
endTime = [2, 5]
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))  # Output: 2

eventTime = 5
k = 1
startTime = [1, 3]
endTime = [2, 5]
output = 2

# TS 2
# eventTime = 10
# k = 1
# startTime = [0, 2, 9]
# endTime = [1, 4, 10]
# Output = 6

# # TS 3
# eventTime = 5
# k = 2
# startTime = [0, 1, 2, 3, 4]
# endTime = [1, 2, 3, 4, 5]
# Output = 0

# TS 3
eventTime = 31
k = 1
startTime = [7, 10, 16]
endTime = [10, 14, 18]
output = 7
print(Solution().maxFreeTime(eventTime, k, startTime, endTime))
