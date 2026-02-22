def merge_intervals(intervals):
    n = len(intervals)

    for i in range(n):
        for j in range(i+1, n):
            if intervals[i][0] > intervals[j][0]:
                intervals[i], intervals[j] = intervals[j], intervals[i]

    res = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, n):
        if intervals[i][0] <= end:
            if intervals[i][1] > end:
                end = intervals[i][1]
        else:
            res.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]

    res.append([start, end])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))