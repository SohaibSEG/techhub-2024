
meetings = [[2,10],[0,2],[15,20]]


def can_attend_all(meetings):
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    for i in range(1,len(sorted_meetings)):
        if sorted_meetings[i][0] < sorted_meetings[i-1][1]:
            print("Can't attend the meeting")
            print("Meeting",sorted_meetings[i])
            return False
    print("Can attend all the meetings")
    return True

can_attend_all(meetings)
