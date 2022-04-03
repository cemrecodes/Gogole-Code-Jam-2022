# GOOGLE CODE JAM 2022
# 02.04.2022

t = int(input())

def solve(n,s):
    s.sort()
    ans = 0
    flag = 0
    counter = 0
    for i in range(0,n-1):
        if (s[i] < s[i+1]):
            counter = i+1
            ans+=1
        i+=1
    for i in range(ans,n):
        if (ans < s[i]):
            ans+=1

    if (ans > n):
        ans = n
    return ans
            
for i in range(1, t + 1):
    n = int(input())
    s = [None]*n
    s[0:n] = [int(a) for a in input().split(" ")]
    print("Case #{}: {}".format(i,solve(n,s)))
    