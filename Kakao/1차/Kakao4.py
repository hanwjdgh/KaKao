"""
1	1	5	["08:00", "08:01", "08:02", "08:03"]	"09:00"
2	10	2	["09:10", "09:09", "08:00"]	"09:09"
2	1	2	["09:00", "09:00", "09:00", "09:00"]	"08:59"
1	1	5	["00:01", "00:01", "00:01", "00:01", "00:01"]	"00:00"
1	1	1	["23:59"]	"09:00"
10	60	45	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	"18:00"
"""

def bus(n,t,m,timetable):
    table = [[0 for cols in range(m+1)]for rows in range(n)]
    b_list = []
    start = 900
    answer =""
    for i in range(0,n):
        b_list.append(start)
        table[i].pop(0)
        table[i].insert(0,start)
        start += (t if t<59 else (t%60+(t//60)*100))
    timetable = sorted(timetable)

    rows, cols = 0, 1
    for i, vars in enumerate(timetable):
        timetable[i] = int(vars[:2])*100+int(vars[3:])
        if timetable[i] > table[rows][0]:
            rows, cols = rows+1, 1
        if cols == m+1:
            rows, cols = rows+1, 1
        if rows == n:
            break
        table[rows].pop(cols)
        table[rows].insert(cols,timetable[i])
        cols += 1

    temp = 0
    for i in range(n-1,-1,-1):
        if temp == 0:
            if 0 in table[i]:
                answer = table[i][0]
                temp = table[i][0]
            else:
                if n==1:
                    answer = table[i][1]-1
                else:
                    temp = table[i][1]
        else:
            if 0 in table[i]:
                answer = temp
            else:
                if temp in table[i]:
                    answer = temp-1
                else:
                    answer = table[i][m]

    if answer % 100 > 59:
        answer -= 40
    answer = str(answer)
    for i in range(0,4-len(answer)):
        answer = "0"+answer
    print('"{}:{}"'.format(answer[:2],answer[2:]))

bus(1,1,5,["08:00", "08:01", "08:02", "08:03"])
bus(2,10,2,["09:10", "09:09", "08:00"])
bus(2,1,2,["09:00", "09:00", "09:00", "09:00"])
bus(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])
bus(1,1,1,["23:59"])
bus(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])