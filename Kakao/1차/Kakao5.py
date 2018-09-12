"""
FRANCE	french	16384
handshake	shake hands	65536
aa1+aa2	AAAA12	43690
E=M*C^2	e=m*c^2	65536
"""

def jakad(str1,str2):
    sub_list1,sub_list2 = [], []
    dic1,dic2 ={}, {}
    kyu, hap = [], []
    str1,str2 = str1.upper(), str2.upper()
    answer = 0

    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            sub_list1.append(str1[i:i+2])
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            sub_list2.append(str2[i:i+2])

    for i in range(0, len(sub_list1)):
        if not sub_list1[i] in dic1:
            dic1.update({sub_list1[i]: sub_list1.count(sub_list1[i])})
    for i in range(0, len(sub_list2)):
        if not sub_list2[i] in dic2:
            dic2.update({sub_list2[i]: sub_list2.count(sub_list2[i])})

    for key,value in dic1.items():
        v_max,v_min = 0,0
        if key in dic2:
            if dic1[key] >= dic2[key]:
                v_max = dic1[key]
                v_min = dic2[key]
            else:
                v_max = dic2[key]
                v_min = dic1[key]
            kyu+=[key for i in range(0,v_min)]
            hap+=[key for i in range(0,v_max)]
        else:
            hap+=[key for i in range(0,value)]

    for key,value in dic2.items():
        if not key in hap:
            hap+=[key for i in range(0,value)]

    if len(hap)==0:
        answer = 1
    else:
        answer =(len(kyu)/len(hap))
    print(int(answer*65536))

jakad("FRANCE","french")
jakad("handshake","shake hands")
jakad("aa1+aa2","AAAA12")
jakad("E=M*C^2","e=m*c^2")