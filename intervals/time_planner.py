def meeting_planner(slotsA, slotsB, dur):
    a_pointer = 0
    b_pointer = 0

    while a_pointer < len(slotsA) and b_pointer < len(slotsB):
        max_start = max(slotsA[a_pointer][0], slotsB[b_pointer][0])
        min_end = min(slotsA[a_pointer][1], slotsB[b_pointer][1])

        if max_start + dur <= min_end:
            return [max_start, max_start + dur]

        if slotsA[a_pointer][1] < slotsB[b_pointer][1]:
            a_pointer += 1
        else:
            b_pointer += 1

    return []

"""
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

Approach:

Find a slot where it's start time is >= the other start time and 
it's end time should be <= the other end time. This can also be done by
finding the max of the start times and the min of the end times

1.  Loop until both pointers reach end of array
2.  Find max of both start times
3.  Find min of both end times
4.  Add dur to the start time
5.  If it is less than the end time, return True
6.  Return empty array

Time    : O(n + m)
Space   : O(1)
"""
slotsA = [[6,12]]
slotsB = [[2,11]]
dur = 5

print(meeting_planner(slotsA, slotsB, dur))