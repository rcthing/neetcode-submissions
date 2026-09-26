class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        curent = intervals[0]
        mini = 0

        for i in range(1, len(intervals)):
            if curent[1] > intervals[i][0]:
                mini += 1
                if curent[1] > intervals[i][1]:
                    curent = intervals[i]
            else:
                curent = intervals[i]

        return mini

