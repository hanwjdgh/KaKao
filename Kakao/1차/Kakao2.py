"""
1	1S2D*3T	37	1^1 * 2 + 2^2 * 2 + 3^3
2	1D2S#10S	9	1^2 + 2^1 * (-1) + 10^1
3	1D2S0T	3	1^2 + 2^1 + 0^3
4	1S*2T*3S	23	1^1 * 2 * 2 + 2^3 * 2 + 3^1
5	1D#2S*3S	5	1^2 * (-1) * 2 + 2^1 * 2 + 3^1
6	1T2D3D#	-4	1^3 + 2^2 + 3^2 * (-1)
7	1D2S3T*	59	1^2 + 2^1 * 2 + 3^3 * 2
"""
import re

d_num = {
    "S" : 1,
    "D" : 2,
    "T" : 3
}

def dart(str):
    numbers,chars = [], []
    cnt = 0
    numbers = re.findall("\d+",str)
    str = re.sub("\d+","",str)
    chars = re.findall("\w|\W",str)
    for i,vars in enumerate(chars):
        if vars == '*':
            if cnt > 1:
                numbers[cnt-2]*=2
                numbers[cnt-1]*=2
            else:
                numbers[cnt-1]*=2
        elif vars == '#':
            numbers[cnt-1] *= -1
        else:
            numbers[cnt] = pow(int(numbers[cnt]),d_num[vars])
            cnt+=1
    return sum(numbers)

print(dart("1S2D*3T"))
print(dart("1D2S#10S"))
print(dart("1D2S0T"))
print(dart("1S*2T*3S"))
print(dart("1D#2S*3S"))
print(dart("1T2D3D#"))
print(dart("1D2S3T*"))