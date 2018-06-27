def solution(x):
    list = [int(i) for i in str(x)]
    if x%sum(list) == 0:
    	return True
    else:
        return False