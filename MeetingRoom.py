can_attend = [0,0]
meetings = [[2,10],[0,2],[15,20]]


def can_attend_all(meetings):
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    for i in range(len(sorted_meetings)):
        if sorted_meetings[i][0] < can_attend[1]:
            print("Can't attend the meeting")
            print("Meeting",sorted_meetings[i])
            return False
        else:
            can_attend[0] = min(sorted_meetings[i][0], can_attend[0])
            can_attend[1] = max(sorted_meetings[i][1], can_attend[1])
        
    print("Can attend all the meetings")
    return True

can_attend_all(meetings)