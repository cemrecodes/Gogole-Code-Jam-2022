# GOOGLE CODE JAM 2022
# 02.04.2022

def solve(r,c):

                 print("Case #{}:".format(i+1)) 
                 counter = 0
                 str1 = ".."
                 str2 = (c-1) * "+-"+"+"
                 str3 = (c-1)*"|."+"|"
                 print("{}{}".format(str1,str2))
                 print("{}{}".format(str1,str3))
                 while counter+1 != r:
                         str4 = c * "+-"+"+"
                         str5 = c*"|."+"|"
                         print("{}".format(str4))
                         print("{}".format(str5))
                         counter+=1
                 str6 = c * "+-"+"+"
                 print("{}".format(str6))
    #return "{} {} {}".format(, b, c)

t = int(input())


for i in range(0, t):
        r, c = [int(s) for s in input().split(" ")] 
        solve(r,c)