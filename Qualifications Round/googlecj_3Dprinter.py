# GOOGLE CODE JAM 2022
# 02.04.2022


t = int(input())

r = t*[4*[0]]
m = t*[4*[0]]
y = t*[4*[0]]
k = t*[4*[0]]



a = [None] * 4

for i in range(0,t):
    for j in range(0,3):
        r[i][j], m[i][j], y[i][j], k[i][j] = [int(s) for s in input().split(" ")]
    a[0] = r[i][0]+m[i][0]+y[i][0]+k[i][0]
    a[1] = r[i][1]+m[i][1]+y[i][1]+k[i][1]
    a[2] = r[i][2]+m[i][2]+y[i][2]+k[i][2]
    if (a[0]<10**6 or a[1]<10**6 or a[2]<10**6):
        print("Case #{}: IMPOSSIBLE".format(i+1))
    else:
        b = min(r[i][0],r[i][1],r[i][2])
        c = min(m[i][0],m[i][1],m[i][2])
        d = min(y[i][0],y[i][1],y[i][2])
        e = min(k[i][0],k[i][1],k[i][2])
        if ( b >= 10**6):
            print("Case #{}: {} {} {} {}".format(i+1,1000000,0,0,0))
        elif ( c >= 10**6):
            print("Case #{}: {} {} {} {}".format(i+1,0,1000000,0,0))
        elif ( d >= 10**6):
            print("Case #{}: {} {} {} {}".format(i+1,0,0,1000000,0))
        elif ( e >= 10**6):
            print("Case #{}: {} {} {} {}".format(i+1,0,0,0,1000000))
        else:
            if ( b+c >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1,b,(1000000-b),0,0))
            elif ( b+d >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1, b,0,(1000000-b),0))
            elif ( b+e >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1, b,0,0,(1000000-b)))
            elif ( c+d >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1, 0,c,(1000000-c),0))
            elif ( c+e >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1, 0,c,0,(1000000-c)))
            elif ( d+e >= 10**6):
                print("Case #{}: {} {} {} {}".format(i+1,0,0,d,(1000000-d)))
            else:
                if ( b+c+d >= 10**6):
                    print("Case #{}: {} {} {} {}".format(i+1, b,c,(1000000-(b+c)),0))
                elif ( b+c+e >= 10**6):
                    print("Case #{}: {} {} {} {}".format(i+1, b,c,0,(1000000-(b+c))))
                elif ( b+d+e >= 10**6):
                    print("Case #{}: {} {} {} {}".format(i+1, b,0,d,(1000000-(b+d))))
                elif ( c+d+e >= 10**6):
                    print("Case #{}: {} {} {} {}".format(i+1, 0,c,d,(1000000-(c+d))))
                else:
                    if ( b+c+d+e >= 10**6):
                        print("Case #{}: {} {} {} {}".format(i+1,b,c,d,(1000000-(b+c+d))))
                    else:
                        print("Case #{}: IMPOSSIBLE".format(i+1))