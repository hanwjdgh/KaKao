"""
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	[“Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”, “Jeju”, “Pangyo”, “Seoul”]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	[“Jeju”, “Pangyo”, “NewYork”, “newyork”]	16
0	[“Jeju”, “Pangyo”, “Seoul”, “NewYork”, “LA”]	25
"""

def LRU(c_size,list):
    hap = 0
    cnt = 0
    c_list = []
    for i,vars in enumerate(list):
        vars = vars.lower()
        if c_size == 0:
            hap += 5
        else:
            if c_size > len(c_list):
                if vars not in c_list:
                    c_list.append(vars)
                    hap += 5
            elif vars in c_list:
                    hap += 1
            else:
                c_list[cnt] = vars
                hap += 5
                cnt += 1

        if cnt == c_size:
            cnt = 0
    return hap  


print(LRU(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(LRU(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(LRU(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(LRU(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(LRU(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(LRU(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))