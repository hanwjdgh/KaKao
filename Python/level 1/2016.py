def solution(a, b):
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    return day[((sum(mon[0:a-1])+b)%7)-1]