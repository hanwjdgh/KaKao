"""
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]

n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
"""
def secret(n,arr1,arr2):
    answer=[]
    for i in range(0,n):
        tem = bin(arr1[i]|arr2[i])[2:].zfill(n)
        tem = tem.replace('1','#')
        tem = tem.replace('0',' ')
        answer.append(tem)
    return answer
    
print(secret(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(secret(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))