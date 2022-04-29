'''
@Cemre
'''

def solve(liste,k):
    # print(liste)
    counter = 0
    i = 0
    j = len(liste)-1
    num = liste[0]
    l = len(liste)
    
    # print(len(liste))
    # print(i ,j)
    while(i != j):
        if counter == 0:
            willsell = liste[i]
            if willsell>liste[j]:
                willsell = liste[j]
                num = willsell
                j -= 1
                counter += 1
            else:
                i += 1
                num = willsell
                counter += 1
    
        else:
            willsell = liste[i]
            if willsell>liste[j]:
                willsell = liste[j]
                j -= 1
                if willsell >= num:
                    counter += 1 
                    num = willsell
                
            else:
                if willsell >= num:
                    counter += 1 
                    num = willsell
                i += 1
                
        # print("i: ",i,"j: ",j,"counter: ",counter,"littlest: ",littlest)
                
                

    if l == 2:
        counter = 2
    elif l == 1:
        counter = 1
    else:
                        
        if num <= liste[i]:
            counter += 1
            
    print("Case #{}: {}".format(k+1,counter)) 
    #print("{}".format(result))                     

t = int(input())
liste = []
for i in range(0,t):
    a = int(input())
    # for j in range(0,a):
    liste.append([int(s) for s in input().split(" ")])
    # print(liste)
        # e = int(input())
        # list.append(e)
    solve(liste[i],i)