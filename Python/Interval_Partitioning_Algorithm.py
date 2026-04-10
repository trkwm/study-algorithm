def Interval_Partitioning_Algorithm(Intervals):
    Intervals.sort()
    schedules = [[]]
    for interval in Intervals:
        added = False
        for index in range(len(schedules)):
            if not schedules[index]:
                schedules[index].append(interval)
                added = True
                break
            else:
                if schedules[index][-1][-1] <= interval[0]:
                    schedules[index].append(interval)
                    added = True
                    break
                else:
                    continue
        if not added:
            schedules.append([interval])
    return schedules

#===================================================================#
Intervals = [[1,4],[2,5],[3,6],[4,7],[5,8],[7,9]]
print(Interval_Partitioning_Algorithm(Intervals))