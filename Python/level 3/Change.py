def solution(n, money):
    dp = [0 for i in range(n+1)]
    
    dp[0] = 1
    leng = len(money)

    for i in range(leng):
        for j in range(1,n+1):
            if j >= money[i]:
                dp[j] += dp[j-money[i]] % 1000000007
    return dp[n]