class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# 典型问题：区间合并
		# 方法是对区间的左边界排序，然后再判断是否有overlap
        intervals.sort(key=lambda x: x[0], reverse=False)
        result = []
        if len(intervals) < 2:
            return intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
            else:
				# 这里的逻辑搞清楚：指针对向i，但我们只能判断i-1是否有overlap
                result.append(intervals[i-1])
        result.append(intervals[i])
        return result
